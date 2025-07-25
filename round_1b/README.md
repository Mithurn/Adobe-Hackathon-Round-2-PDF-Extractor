# Intelligent Document Analyst System

This system extracts and prioritizes relevant sections from PDF documents based on a specific persona and their job-to-be-done.

## System Requirements

- Docker
- CPU-only execution
- Model size ≤ 1GB
- Processing time ≤ 60 seconds for 3-5 documents

## Build Instructions

1. Navigate to the project directory:
   ```bash
   cd document_analyst
   ```

2. Build the Docker image:
   ```bash
   docker build -t document-analyst .
   ```

## Execution Instructions

1. Prepare your input data:
   - Create a directory with your PDF files
   - Create a `challenge1b_input.json` file following the required format

2. Run the Docker container:
   ```bash
   docker run -v /path/to/your/input:/app/input -v /path/to/your/output:/app/output document-analyst
   ```

   Replace `/path/to/your/input` with the absolute path to your input directory containing:
   - `challenge1b_input.json`
   - `PDFs/` directory with your PDF files

   Replace `/path/to/your/output` with the absolute path where you want the output file saved.

## Input Format

The `challenge1b_input.json` file should follow this structure:

```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [
    {"filename": "doc.pdf", "title": "Title"}
  ],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Use case description"}
}
```

## Output Format

The system generates `challenge1b_output.json` with the following structure:

```json
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description",
    "processing_timestamp": "ISO timestamp"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```

## Example Usage

```bash
# Build the image
docker build -t document-analyst .

# Run with sample data
docker run -v $(pwd)/sample_input:/app/input -v $(pwd)/sample_output:/app/output document-analyst
```

## Architecture

The system consists of several modular components:

1. **PDF Processor**: Extracts text content from PDF files
2. **Section Parser**: Identifies and structures document sections
3. **Relevance Analyzer**: Ranks sections based on persona and job-to-be-done
4. **Output Generator**: Formats results into the required JSON structure

## Performance Characteristics

- CPU-only execution using lightweight libraries
- TF-IDF and cosine similarity for semantic analysis
- Rule-based section identification
- Optimized for processing 3-5 documents within 60 seconds

