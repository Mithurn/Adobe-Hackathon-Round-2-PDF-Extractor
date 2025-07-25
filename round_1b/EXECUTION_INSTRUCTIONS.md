# Execution Instructions for Intelligent Document Analyst System

## Overview

This document provides comprehensive instructions for building, deploying, and executing the Intelligent Document Analyst System. The system is designed to extract and prioritize relevant sections from PDF documents based on a specific persona and their job-to-be-done, adhering to strict constraints of CPU-only execution, model size limitations, and processing time requirements.

## System Requirements

### Hardware Requirements
- CPU-only execution (no GPU required)
- Minimum 2GB RAM
- 1GB available disk space

### Software Requirements
- Docker (version 20.0 or higher)
- Operating System: Linux, macOS, or Windows with Docker support

### Performance Constraints
- Model size: ≤ 1GB
- Processing time: ≤ 60 seconds for 3-5 documents
- CPU-only execution

## Build Instructions

### Step 1: Prepare the Environment

1. Ensure Docker is installed and running on your system:
   ```bash
   docker --version
   ```

2. Clone or extract the project files to your local directory.

3. Navigate to the project root directory:
   ```bash
   cd /path/to/document_analyst
   ```

### Step 2: Build the Docker Image

Execute the following command to build the Docker image:

```bash
docker build -t document-analyst .
```

This command will:
- Use Python 3.11-slim as the base image
- Install required Python dependencies (pypdf, scikit-learn, etc.)
- Copy the source code into the container
- Set up the necessary directory structure

### Step 3: Verify the Build

Confirm the image was built successfully:

```bash
docker images | grep document-analyst
```

## Input Data Preparation

### Directory Structure

Create the following directory structure for your input data:

```
input_directory/
├── challenge1b_input.json
└── PDFs/
    ├── document1.pdf
    ├── document2.pdf
    └── document3.pdf
```

### Input JSON Format

The `challenge1b_input.json` file must follow this exact structure:

```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "your_test_case_name",
    "description": "Brief description of the test case"
  },
  "documents": [
    {"filename": "document1.pdf", "title": "Document 1 Title"},
    {"filename": "document2.pdf", "title": "Document 2 Title"},
    {"filename": "document3.pdf", "title": "Document 3 Title"}
  ],
  "persona": {
    "role": "Your Persona Description (e.g., PhD Researcher in Computational Biology)"
  },
  "job_to_be_done": {
    "task": "Your specific task description (e.g., Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks)"
  }
}
```

### PDF Requirements

- PDF files must be placed in the `PDFs/` subdirectory
- Filenames in the JSON must exactly match the actual PDF filenames
- PDFs should contain extractable text (not scanned images)
- Recommended: 3-5 documents for optimal performance

## Execution Instructions

### Basic Execution

Run the Docker container with the following command:

```bash
docker run -v /absolute/path/to/input:/app/input -v /absolute/path/to/output:/app/output document-analyst
```

Replace the paths with your actual directories:
- `/absolute/path/to/input`: Directory containing `challenge1b_input.json` and `PDFs/` folder
- `/absolute/path/to/output`: Directory where `challenge1b_output.json` will be saved

### Example Execution

```bash
# Example with specific paths
docker run -v /home/user/test_data:/app/input -v /home/user/results:/app/output document-analyst

# Example using current directory
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output document-analyst
```

### Execution with Logging

To see detailed processing logs:

```bash
docker run -v /path/to/input:/app/input -v /path/to/output:/app/output document-analyst 2>&1 | tee execution.log
```

## Output Format

### Output File Location

The system generates `challenge1b_output.json` in the specified output directory.

### Output Structure

```json
{
  "metadata": {
    "input_documents": ["list of input PDF filenames"],
    "persona": "Persona role from input",
    "job_to_be_done": "Task description from input",
    "processing_timestamp": "ISO 8601 timestamp"
  },
  "extracted_sections": [
    {
      "document": "source_document.pdf",
      "section_title": "Section Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source_document.pdf",
      "refined_text": "Most relevant text snippet from the section",
      "page_number": 1
    }
  ]
}
```

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Docker command not found"
**Solution**: Install Docker following the official installation guide for your operating system.

#### Issue: "Permission denied" when running Docker
**Solution**: 
- On Linux: Add your user to the docker group or use `sudo`
- On Windows/macOS: Ensure Docker Desktop is running

#### Issue: "Input file not found"
**Solution**: 
- Verify the input directory path is absolute
- Ensure `challenge1b_input.json` exists in the input directory
- Check that PDF files exist in the `PDFs/` subdirectory

#### Issue: "Processing takes too long"
**Solution**: 
- Reduce the number of input documents
- Ensure PDFs contain extractable text (not scanned images)
- Check system resources (CPU, memory)

#### Issue: "Empty or invalid output"
**Solution**: 
- Verify input JSON format is correct
- Check that PDF files are readable
- Ensure persona and job-to-be-done fields are meaningful

### Performance Optimization

1. **Document Size**: Limit individual PDF files to reasonable sizes (< 50 pages recommended)
2. **Number of Documents**: Process 3-5 documents at a time for optimal performance
3. **Text Quality**: Use PDFs with clear, extractable text rather than scanned documents
4. **System Resources**: Ensure adequate CPU and memory resources are available

## Testing the System

### Using Provided Test Data

The system includes test data in the `test_input/` directory:

```bash
docker run -v $(pwd)/test_input:/app/input -v $(pwd)/test_output:/app/output document-analyst
```

### Validating Output

1. Check that `challenge1b_output.json` is created in the output directory
2. Verify the JSON structure matches the expected format
3. Confirm that sections are ranked by importance
4. Ensure subsection analysis contains relevant text snippets

## Advanced Usage

### Custom Configuration

The system can be customized by modifying the source code:

1. **Ranking Algorithm**: Modify `relevance_analyzer.py` to adjust scoring weights
2. **Section Detection**: Update `section_parser.py` to improve section identification
3. **Text Processing**: Enhance `pdf_processor.py` for better text extraction

### Integration with Other Systems

The Docker container can be integrated into larger workflows:

```bash
# Example: Automated processing pipeline
for input_dir in /data/collections/*; do
    output_dir="/results/$(basename $input_dir)"
    mkdir -p "$output_dir"
    docker run -v "$input_dir":/app/input -v "$output_dir":/app/output document-analyst
done
```

## Support and Maintenance

### Logging and Monitoring

- Container logs are available via `docker logs <container_id>`
- Processing timestamps are included in output metadata
- Error messages are written to stderr

### Updates and Modifications

To update the system:

1. Modify source code as needed
2. Rebuild the Docker image: `docker build -t document-analyst .`
3. Test with known data before production use

This comprehensive execution guide ensures reliable deployment and operation of the Intelligent Document Analyst System across various environments and use cases.

