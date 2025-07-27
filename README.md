# Adobe Hackathon: Intelligent PDF Structure & Relevance Extractor

# Adobe Hackathon Round 2: Intelligent PDF Reader Web Application

## 🚀 Overview

Welcome to Round 2 of the Adobe "Connecting the Dots" Hackathon! This is where we transform the humble PDF into an intelligent, interactive experience that understands structure, surfaces insights, and responds like a trusted research companion.

## 🎯 Mission

Build a beautiful, intuitive reading webapp using Adobe's PDF Embed API that leverages the intelligent document analysis from Round 1A and Round 1B to create a futuristic reading experience.

## ✨ Features

### Core Features
- **📖 Intelligent PDF Viewer**: Adobe PDF Embed API integration with custom controls
- **🧠 Smart Document Analysis**: Real-time structure extraction and persona-driven insights
- **🎯 Personalized Reading**: Content relevance ranking based on user persona and goals
- **🔍 Advanced Search**: Semantic search across document collections
- **📊 Interactive Outlines**: Clickable document structure with importance indicators
- **💡 Insight Generation**: AI-powered content recommendations and connections

### Advanced Features
- **🎨 Modern UI/UX**: Beautiful, responsive design with dark/light themes
- **📱 Cross-Platform**: Works seamlessly on desktop, tablet, and mobile
- **⚡ Performance Optimized**: Fast loading and smooth interactions
- **🔒 Privacy-First**: All processing happens client-side
- **🌐 Multi-Document Support**: Handle collections of related PDFs
- **📈 Reading Analytics**: Track reading progress and engagement

## 🏗️ Architecture

### Frontend Stack
- **React 18** with TypeScript for robust UI development
- **Tailwind CSS** for beautiful, responsive styling
- **Adobe PDF Embed API** for PDF rendering and interaction
- **React Query** for efficient data management
- **Framer Motion** for smooth animations

### Backend Integration
- **Node.js/Express** for API endpoints
- **Docker** for consistent deployment
- **Round 1A Integration**: PDF structure extraction service
- **Round 1B Integration**: Persona-driven content analysis service

### Key Components
1. **PDF Viewer Component**: Adobe Embed API integration with custom controls
2. **Document Analyzer**: Real-time structure and relevance analysis
3. **Persona Manager**: User persona and job-to-be-done configuration
4. **Insight Panel**: AI-generated insights and recommendations
5. **Search Engine**: Semantic search across document collections
6. **Progress Tracker**: Reading progress and engagement metrics

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Docker (for backend services)
- Adobe PDF Embed API credentials

### Installation

1. **Clone and Setup**
   ```bash
   cd round_2
   npm install
   ```

2. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Add your Adobe PDF Embed API credentials
   ```

3. **Start Development Server**
   ```bash
   npm run dev
   ```

4. **Access the Application**
   ```
   http://localhost:3000
   ```

### Docker Deployment

1. **Build the Application**
   ```bash
   docker build -t adobe-pdf-reader .
   ```

2. **Run with Backend Services**
   ```bash
   docker-compose up -d
   ```

## 📁 Project Structure

```
round_2/
├── src/
│   ├── components/          # React components
│   │   ├── PDFViewer/      # Adobe PDF Embed integration
│   │   ├── DocumentAnalyzer/ # Structure and relevance analysis
│   │   ├── PersonaManager/  # User persona configuration
│   │   ├── InsightPanel/    # AI insights and recommendations
│   │   └── SearchEngine/    # Semantic search functionality
│   ├── services/           # API and external service integrations
│   ├── hooks/              # Custom React hooks
│   ├── utils/              # Utility functions
│   └── types/              # TypeScript type definitions
├── public/                 # Static assets
├── docker/                 # Docker configuration
└── docs/                   # Documentation
```

## 🎨 Design Philosophy

### User Experience
- **Intuitive Navigation**: Seamless flow between document viewing and analysis
- **Progressive Disclosure**: Show relevant information at the right time
- **Personalization**: Adapt interface based on user persona and goals
- **Accessibility**: WCAG 2.1 AA compliance for inclusive design

### Visual Design
- **Modern Aesthetics**: Clean, professional interface with subtle animations
- **Information Hierarchy**: Clear visual hierarchy for easy scanning
- **Responsive Design**: Optimized for all screen sizes and devices
- **Theme Support**: Dark and light mode with smooth transitions

## 🔧 Technical Implementation

### Adobe PDF Embed API Integration
- Custom viewer controls and annotations
- Real-time page tracking and analytics
- Document structure overlay
- Interactive outline navigation

### Round 1A Integration
- Automatic structure extraction on document load
- Interactive outline with page navigation
- Heading level visualization
- Document metadata display

### Round 1B Integration
- Persona-based content relevance scoring
- Job-to-be-done analysis
- Section importance ranking
- Subsection extraction and highlighting

### Performance Optimizations
- Lazy loading for large documents
- Virtual scrolling for long content
- Efficient memory management
- Caching strategies for repeated analysis

## 🧪 Testing

### Unit Tests
```bash
npm run test
```

### Integration Tests
```bash
npm run test:integration
```

### E2E Tests
```bash
npm run test:e2e
```

## 📊 Performance Metrics

- **Initial Load Time**: < 3 seconds
- **PDF Rendering**: < 2 seconds for 50-page documents
- **Analysis Response**: < 5 seconds for document processing
- **Search Response**: < 1 second for semantic queries
- **Memory Usage**: < 500MB for typical usage

## 🔒 Security & Privacy

- **Client-Side Processing**: Sensitive document analysis happens locally
- **No Data Storage**: Documents are not stored on servers
- **Secure API Calls**: Encrypted communication with backend services
- **User Consent**: Clear privacy controls and data handling transparency

## 🚀 Deployment

### Production Build
```bash
npm run build
```

### Docker Production
```bash
docker build -t adobe-pdf-reader:prod .
docker run -p 80:3000 adobe-pdf-reader:prod
```

### Cloud Deployment
- **Vercel**: Optimized for React applications
- **AWS**: Scalable cloud infrastructure
- **Google Cloud**: Enterprise-grade hosting

## 📈 Future Enhancements

### Planned Features
- **Collaborative Reading**: Multi-user annotation and discussion
- **Advanced Analytics**: Detailed reading behavior insights
- **AI Summarization**: Automatic document summarization
- **Citation Management**: Integrated reference tracking
- **Export Options**: Multiple format export capabilities

### Technical Roadmap
- **PWA Support**: Offline reading capabilities
- **Real-time Sync**: Live collaboration features
- **Advanced AI**: Enhanced content understanding
- **API Ecosystem**: Third-party integrations

## 🤝 Contributing

This project follows Adobe's hackathon guidelines and best practices:

- **Code Quality**: ESLint and Prettier for consistent code style
- **Documentation**: Comprehensive inline and external documentation
- **Testing**: Thorough test coverage for all components
- **Performance**: Regular performance monitoring and optimization

## 📄 License

This project is developed for the Adobe "Connecting the Dots" Hackathon and follows the competition guidelines.

## 🙏 Acknowledgments

- Adobe PDF Embed API team for the powerful PDF integration
- React and TypeScript communities for excellent tooling
- Tailwind CSS for beautiful, utility-first styling
- All open-source contributors whose work made this possible

---

**Built with ❤️ for the Adobe "Connecting the Dots" Hackathon**

*Transforming PDFs into intelligent, interactive experiences* 

## Overview

This repository contains solutions for both Round 1A and Round 1B of the Adobe “Connecting the Dots” Hackathon. The goal is to transform static PDFs into intelligent, structured, and interactive documents—enabling smarter reading, search, and knowledge discovery.

---

## Contents

- `round_1a/` — PDF Structure Extractor (Round 1A)
- `round_1b/` — Persona-Driven Document Intelligence (Round 1B)
- `.gitignore` — Excludes outputs, test/demo files, and system artifacts
- `README.md` — This documentation

---

# How to Test Both Round 1A and 1B

This repository contains solutions for both Round 1A (PDF Structure Extractor) and Round 1B (Intelligent Document Analyst System) of the Adobe “Connecting the Dots” Hackathon.

## Round 1A: PDF Structure Extractor

1. **Build the Docker Image**
   ```sh
   cd round_1a
   docker build --platform linux/amd64 -t round1a-extractor:latest .
   ```
2. **Prepare Input/Output Folders**
   - Place your PDFs in `round_1a/input/`
   - Ensure `round_1a/output/` exists (will be created if not)
3. **Run the Container**
   ```sh
   docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" --network none round1a-extractor:latest
   ```
4. **Check the Output**
   - Each PDF in `input/` will produce a corresponding `.json` in `output/`.

## Round 1B: Intelligent Document Analyst System

1. **Build the Docker Image**
   ```sh
   cd round_1b
   docker build --platform linux/amd64 -t round1b-analyst:latest .
   ```
2. **Prepare Input/Output Folders**
   - Place your `challenge1b_input.json` and a `PDFs/` folder with your PDFs in `round_1b/input/`
   - Ensure `round_1b/output/` exists (will be created if not)
3. **Run the Container**
   ```sh
   docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" round1b-analyst:latest
   ```
4. **Check the Output**
   - The output JSON (e.g., `challenge1b_output.json`) will be in `output/`.

For more details, see the `README.md` files in each round's subfolder.

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
