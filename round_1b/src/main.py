import json
import os
from datetime import datetime
from pdf_processor import extract_text_from_pdf
from section_parser import identify_sections
from relevance_analyzer import rank_sections, analyze_subsections

def process_documents(input_json_path, pdf_dir):
    with open(input_json_path, 'r') as f:
        input_data = json.load(f)

    metadata = {
        "input_documents": [doc["filename"] for doc in input_data["documents"]],
        "persona": input_data["persona"]["role"],
        "job_to_be_done": input_data["job_to_be_done"]["task"],
        "processing_timestamp": datetime.now().isoformat()
    }

    all_sections = []

    for doc_info in input_data["documents"]:
        pdf_filename = doc_info["filename"]
        pdf_path = os.path.join(pdf_dir, pdf_filename)

        print(f"Processing {pdf_filename}...")
        text_content_per_page = extract_text_from_pdf(pdf_path)
        
        sections_from_doc = identify_sections(text_content_per_page, pdf_filename)
        
        for section in sections_from_doc:
            all_sections.append(section)

    # Rank sections
    ranked_sections = rank_sections(all_sections, metadata["persona"], metadata["job_to_be_done"])

    # Analyze subsections from the top-ranked sections (e.g., top 5 or all if less than 5)
    # For the challenge, we need to analyze all sections, not just top-ranked.
    subsection_analysis = analyze_subsections(ranked_sections, metadata["persona"], metadata["job_to_be_done"], num_snippets=1)

    # Format extracted_sections for output
    formatted_extracted_sections = []
    for section in ranked_sections:
        formatted_extracted_sections.append({
            "document": section["document"],
            "section_title": section["section_title"],
            "importance_rank": section["importance_rank"],
            "page_number": section["page_number"]
        })

    output_data = {
        "metadata": metadata,
        "extracted_sections": formatted_extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    return output_data

if __name__ == '__main__':
    # This part is for local testing and will be replaced by Docker entrypoint
    # when creating the Dockerfile.
    
    # Create dummy PDF files for testing
    from reportlab.pdfgen import canvas
    
    # Dummy PDF 1
    pdf1_path = "/home/ubuntu/document_analyst/data/sample_doc1.pdf"
    c = canvas.Canvas(pdf1_path)
    c.drawString(100, 750, "CHAPTER 1: INTRODUCTION TO AI")
    c.drawString(100, 730, "Artificial intelligence (AI) is a rapidly evolving field...")
    c.drawString(100, 710, "SECTION A: HISTORY OF AI")
    c.drawString(100, 690, "Early developments in AI date back to the 1950s...")
    c.showPage()
    c.drawString(100, 750, "CHAPTER 2: MACHINE LEARNING")
    c.drawString(100, 730, "Machine learning is a subset of AI...")
    c.save()
    
    # Dummy PDF 2
    pdf2_path = "/home/ubuntu/document_analyst/data/sample_doc2.pdf"
    c = canvas.Canvas(pdf2_path)
    c.drawString(100, 750, "CHAPTER 1: ORGANIC CHEMISTRY BASICS")
    c.drawString(100, 730, "Organic chemistry is the study of carbon-containing compounds...")
    c.drawString(100, 710, "SECTION B: ALKANES AND ALKENES")
    c.drawString(100, 690, "Alkanes are saturated hydrocarbons...")
    c.showPage()
    c.drawString(100, 750, "CHAPTER 2: REACTION MECHANISMS")
    c.drawString(100, 730, "Understanding reaction mechanisms is crucial...")
    c.save()

    # Dummy input JSON for testing
    dummy_input_data = {
      "challenge_info": {
        "challenge_id": "test_case_001",
        "test_case_name": "dummy_test",
        "description": "Test with dummy PDFs"
      },
      "documents": [
        {"filename": "sample_doc1.pdf", "title": "Introduction to AI"},
        {"filename": "sample_doc2.pdf", "title": "Organic Chemistry"}
      ],
      "persona": {"role": "Student"},
      "job_to_be_done": {"task": "Understand key concepts in AI and Organic Chemistry"}
    }
    
    dummy_input_json_path = "/home/ubuntu/document_analyst/data/dummy_input.json"
    with open(dummy_input_json_path, 'w') as f:
        json.dump(dummy_input_data, f, indent=2)

    output = process_documents(dummy_input_json_path, "/home/ubuntu/document_analyst/data")
    
    output_json_path = "/home/ubuntu/document_analyst/output/dummy_output.json"
    with open(output_json_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Output saved to {output_json_path}")

