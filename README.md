# Adobe Hackathon: Intelligent PDF Structure & Relevance Extractor

## Overview

This repository contains solutions for both Round 1A and Round 1B of the Adobe “Connecting the Dots” Hackathon. The goal is to transform static PDFs into intelligent, structured, and interactive documents—enabling smarter reading, search, and knowledge discovery.

---

## Contents

- `round_1a/` — PDF Structure Extractor (Round 1A)
- `round_1b/` — Persona-Driven Document Intelligence (Round 1B)
- `.gitignore` — Excludes outputs, test/demo files, and system artifacts
- `README.md` — This documentation

---

## Round 1A: PDF Structure Extractor

### Objective

Extract a structured outline (Title, H1, H2, H3 headings with page numbers) from PDF files and output the result as a JSON file, ready for downstream document intelligence tasks.

### Features

- **Document Structure Extraction:** Title, H1, H2, H3 headings with page numbers
- **Batch Processing:** Processes all PDFs in `/app/input` and outputs JSONs to `/app/output`
- **Offline Processing:** No internet required
- **Dockerized:** Consistent, portable deployment
- **No Hardcoding:** Uses robust heuristics, not file-specific logic

### How to Use

1. **Build the Docker Image**
   ```sh
   docker build --platform linux/amd64 -t pdf-structure-extractor:latest ./round_1a
   ```

2. **Prepare Input/Output Folders**
   ```sh
   mkdir -p round_1a/input round_1a/output
   cp yourfile.pdf round_1a/input/
   ```

3. **Run the Container**
   ```sh
   docker run --rm -v "$(pwd)/round_1a/input:/app/input" -v "$(pwd)/round_1a/output:/app/output" --network none pdf-structure-extractor:latest
   ```

4. **Check the Output**
   - Each PDF in `input/` will produce a corresponding `.json` in `output/`.

### Example Output

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

---

## Round 1B: Persona-Driven Document Intelligence

### Objective

Given a collection of PDFs, a persona, and a job-to-be-done, extract and rank the most relevant sections and subsections, outputting a structured JSON for downstream use.

### Features

- **Persona-based Content Analysis:** Tailors extraction to user needs
- **Section & Subsection Ranking:** Importance-based output
- **Batch Processing:** Handles multiple document collections
- **Dockerized:** Consistent, portable deployment

### How to Use

1. **Build the Docker Image**
   ```sh
   docker build --platform linux/amd64 -t pdf-relevance-extractor:latest ./round_1b
   ```

2. **Prepare Input/Output Folders**
   - Place your input JSON and PDFs in the appropriate folders (see `round_1b/README.md` for details).

3. **Run the Container**
   ```sh
   docker run --rm -v "$(pwd)/round_1b/data:/app/data" -v "$(pwd)/round_1b/output:/app/output" --network none pdf-relevance-extractor:latest
   ```

4. **Check the Output**
   - Output JSONs will be saved in the `output/` folder.

---

## General Notes

- **No Hardcoding:** Both solutions use general heuristics and are designed to work on a wide variety of PDFs.
- **No Internet Required:** All processing is offline.
- **Open Source Dependencies:** All libraries are open source and installed via the Dockerfile.
- **Tested on Provided and Custom PDFs:** Solutions are robust and generalize well.

---

## Credits

Developed by Mithurn Jeromme for the Adobe “Connecting the Dots” Hackathon.

For questions or feedback, please contact: [Your Email or GitHub]
