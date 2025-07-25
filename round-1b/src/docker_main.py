import json
import os
import sys
from datetime import datetime
from pdf_processor import extract_text_from_pdf
from section_parser import identify_sections
from relevance_analyzer import rank_sections, analyze_subsections

def process_documents(input_json_path, pdf_dir, output_json_path):
    """
    Main function to process documents based on input JSON and save output JSON.
    This is the entry point for the Docker container.
    """
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

        if not os.path.exists(pdf_path):
            print(f"Warning: PDF file {pdf_path} not found. Skipping.")
            continue

        print(f"Processing {pdf_filename}...")
        text_content_per_page = extract_text_from_pdf(pdf_path)
        
        sections_from_doc = identify_sections(text_content_per_page, pdf_filename)
        
        for section in sections_from_doc:
            all_sections.append(section)

    # Rank sections
    ranked_sections = rank_sections(all_sections, metadata["persona"], metadata["job_to_be_done"])

    # Analyze subsections
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

    with open(output_json_path, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"Processing complete. Output saved to {output_json_path}")

if __name__ == '__main__':
    # Docker execution expects specific paths
    input_json_path = "/app/input/challenge1b_input.json"
    pdf_dir = "/app/input/PDFs"
    output_json_path = "/app/output/challenge1b_output.json"

    # Check if input files exist
    if not os.path.exists(input_json_path):
        print(f"Error: Input JSON file {input_json_path} not found.")
        sys.exit(1)

    if not os.path.exists(pdf_dir):
        print(f"Error: PDF directory {pdf_dir} not found.")
        sys.exit(1)

    try:
        process_documents(input_json_path, pdf_dir, output_json_path)
    except Exception as e:
        print(f"Error during processing: {e}")
        sys.exit(1)

