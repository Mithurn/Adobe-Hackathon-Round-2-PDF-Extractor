
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    text_content = []
    try:
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages):
            text_content.append({
                "page_number": page_num + 1,
                "text": page.extract_text() or ""
            })
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
    return text_content

if __name__ == '__main__':
    # Example usage (for testing purposes)
    # This part will not be executed in the final Dockerized solution
    # as input will come from the main script.
    sample_pdf_path = "/home/ubuntu/document_analyst/data/sample.pdf" # Placeholder
    # Create a dummy PDF for testing if it doesn't exist
    try:
        from reportlab.pdfgen import canvas
        c = canvas.Canvas(sample_pdf_path)
        c.drawString(100, 750, "This is a sample PDF document.")
        c.drawString(100, 730, "It has multiple lines of text.")
        c.showPage()
        c.drawString(100, 750, "This is the second page.")
        c.save()
    except ImportError:
        print("ReportLab not installed. Cannot create dummy PDF for testing.")
        print("Please install it using: pip install reportlab")

    extracted_data = extract_text_from_pdf(sample_pdf_path)
    for page_data in extracted_data:
        print(f"Page {page_data['page_number']}:\n{page_data['text']}\n---")


