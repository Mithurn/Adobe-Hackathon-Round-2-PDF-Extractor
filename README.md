# Adobe Hackathon Round 1A: PDF Structure Extractor

## Overview
This project is a solution for Round 1A of the Adobe “Connecting the Dots” Hackathon. The goal is to extract a structured outline (Title, H1, H2, H3 headings with page numbers) from PDF files and output the result as a JSON file, ready for downstream document intelligence tasks.

## Features
- **Document Structure Extraction:** Extracts title, H1, H2, and H3 headings with page numbers
- **Batch Processing:** Processes all PDFs in `/app/input` and outputs JSONs to `/app/output`
- **Offline Processing:** PDF structure extraction works without internet connectivity
- **Docker Support:** Containerized solution for consistent deployment
- **JSON Output:** Structured output in the required format

## Approach
- **PDF Parsing:** Utilizes PyMuPDF for robust PDF text and font extraction.
- **Heading Detection:** Groups text by font size and style, then applies heuristics to classify headings (H1, H2, H3) and extract the document title.
- **Composite Title Extraction:** Concatenates the top 2–3 largest-font lines at the top of the first page, preserving spaces.
- **Outline Filtering:** Only includes true section headings, not dates, metadata, or table entries. Assigns heading levels based on font size and structure.
- **No Hardcoding:** The extractor uses general heuristics and does not hardcode for specific files or demo outputs.

## How to Use

### 1. Build the Docker Image
```sh
docker build --platform linux/amd64 -t pdf-structure-extractor:latest ./round_1a
```

### 2. Prepare Input/Output Folders
Place your PDFs in an `input` folder:
```sh
mkdir -p round_1a/input round_1a/output
cp yourfile.pdf round_1a/input/
```

### 3. Run the Container
```sh
docker run --rm -v "$(pwd)/round_1a/input:/app/input" -v "$(pwd)/round_1a/output:/app/output" --network none pdf-structure-extractor:latest
```

### 4. Check the Output
Each PDF in `input/` will produce a corresponding `.json` in `output/`.

## Example Output
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## Folder Structure
- `round_1a/input/` — Place your input PDFs here
- `round_1a/output/` — Extracted JSONs will be saved here
- `round_1a/pdf_extractor.py` — Main extraction script
- `round_1a/Dockerfile` — Docker configuration

## Testing
- Place sample PDFs in `round_1a/input/` and run the Docker container as above.
- Compare the output JSONs in `round_1a/output/` to the expected structure.

## Notes
- The extractor is designed to generalize to a wide variety of PDFs and does not use any file-specific logic.
- All dependencies are open source and installed via the Dockerfile.
- No internet access is required for processing.

## Credits
Developed by Mithurn Jeromme for the Adobe “Connecting the Dots” Hackathon.

---
For questions or feedback, please contact: [Your Email or GitHub]
