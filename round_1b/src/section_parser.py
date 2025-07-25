import re

def identify_sections(text_content, document_filename):
    sections = []
    current_section = None
    section_counter = 0

    for page_data in text_content:
        page_number = page_data["page_number"]
        text = page_data["text"]
        lines = text.split("\n")

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Heuristic: Identify potential section titles (e.g., all caps, bold, large font - simulated by length and case)
            # This is a simplified heuristic and would need refinement for real-world PDFs
            if len(line) > 5 and len(line) < 100 and line.isupper() and not line.isdigit():
                if current_section:
                    sections.append(current_section)
                section_counter += 1
                current_section = {
                    "document_filename": document_filename,
                    "section_id": f"section_{section_counter}",
                    "section_title": line,
                    "page_number": page_number,
                    "content": []
                }
            elif current_section:
                current_section["content"].append(line)
            else:
                # If no section title is found yet, treat as part of an implicit first section
                if not sections and not current_section:
                    section_counter += 1
                    current_section = {
                        "document_filename": document_filename,
                        "section_id": f"section_{section_counter}",
                        "section_title": "Introduction" if section_counter == 1 else f"Untitled Section {section_counter}",
                        "page_number": page_number,
                        "content": []
                    }
                current_section["content"].append(line)

    if current_section:
        sections.append(current_section)

    # Join content lines into a single string for each section
    for section in sections:
        section["content"] = " ".join(section["content"])

    return sections

if __name__ == '__main__':
    # Dummy text content for testing
    sample_text_content = [
        {"page_number": 1, "text": "CHAPTER 1\nINTRODUCTION\nThis is the introduction to the document. It talks about various things.\nMore introductory text.\n"},
        {"page_number": 1, "text": "\nSECTION A: BACKGROUND\nHere is some background information. It is quite important.\n"},
        {"page_number": 2, "text": "\nCHAPTER 2\nMETHODOLOGY\nThis chapter describes the methods used. Method one. Method two.\n"},
        {"page_number": 2, "text": "\nSUBSECTION 2.1: DATA COLLECTION\nData was collected using surveys.\n"}
    ]

    parsed_sections = identify_sections(sample_text_content, "dummy_doc.pdf")
    for section in parsed_sections:
        print(f"Section ID: {section['section_id']}")
        print(f"Title: {section['section_title']}")
        print(f"Page: {section['page_number']}")
        print(f"Content: {section['content'][:100]}...") # Print first 100 chars
        print("---")

