# Intelligent Web Browser Query Agent for Ripplica

![Project Logo or Banner - Optional]

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture & Workflow](#architecture--workflow)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Validation Heuristics](#validation-heuristics)
- [Similarity Search & Caching](#similarity-search--caching)
- [Web Scraping & Summarization](#web-scraping--summarization)
- [Engineering Decisions](#engineering-decisions)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

This project implements an intelligent web browser query agent developed for **Ripplica**, led by CEO Bhavesh. It enables users to submit natural language queries that are validated, efficiently matched against cached similar queries using semantic embeddings, and, if new, answered by scraping relevant web content followed by AI-powered summarization. The agent balances speed, maintainability, and reliability to deliver concise, meaningful responses promptly.

---

## Features

- Fast query validation using lightweight heuristics  
- Semantic similarity search with SentenceTransformer embeddings and ChromaDB vector search  
- Automated scraping of top 5 search results via Playwright  
- AI-based summarization using OpenAI GPT, Google Gemini API, and Hugging Face models  
- Caching of query-summary pairs to avoid redundant work  
- Modular architecture supporting scalability and future improvements  

---

## Architecture & Workflow

![Flowchart illustrating the system architecture and workflow](./docs/images/flowchart.png)

*Figure: System flow from query submission, through validation, semantic caching, scraping, summarization, to final response.*

The core processing flow:

1. User submits a query.  
2. The query is validated using simple heuristics to ensure meaningful input.  
3. If valid, the system searches a cache of past queries in ChromaDB using semantic embedding similarity.  
4. If a close match is found (cosine similarity under threshold), the cached summary is returned instantly.  
5. If no cached summary exists, Playwright automates a browser to scrape the top 5 search results from DuckDuckGo.  
6. The scraped content is summarized into a concise answer using AI language models.  
7. The new query and summary are cached for future reuse.  
8. The summary is returned to the user.

---

## Technology Stack

- **Backend:** FastAPI (Python) for API and processing  
- **Frontend:** React.js for user interface (optional)  
- **Web Scraping:** Playwright for robust headless browser automation  
- **Semantic Search:** SentenceTransformer `all-MiniLM-L6-v2` embeddings + ChromaDB vector database  
- **AI Summarization:** OpenAI GPT, Google Gemini API, Hugging Face models for diverse summarization options  
- **Utilities:** UUID for unique caching keys, Python logging for traceability  

---

## Installation

### Prerequisites

- Python 3.10+ for FastAPI backend  
- Node.js and npm/yarn for React frontend and Playwright dependencies  
- Access to AI API keys (Gemini, OpenAI, Hugging Face) configured via environment variables  

### Setup Instructions

```
# Clone the repository
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

# Backend setup: install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers required for scraping
playwright install

# Frontend setup (if separate frontend folder)
cd frontend
npm install
npm start  # to run React development server

# Run the backend API server from project root
uvicorn app:app --host 0.0.0.0 --port 8000  --log-level debug
```

---

## Usage

- Submit queries via the API endpoint or through the React frontend client.  
- The system returns quick answers by validating, caching, scraping, and summarizing queries in near real-time.  
- Cached results speed up repeated queries with similar meaning.

---

## Validation Heuristics

The system uses **simple, fast heuristics** to validate user queries by checking:  
- Presence of interrogative words (e.g., what, how, why) or question marks anywhere  
- Inclusion of comparator keywords (e.g., best, worst, top)  
- Avoidance of multiple unrelated commands separated by commas, semicolons, or conjunctions  
This lightweight filtering ensures responsiveness without heavy NLP processing.

---

## Similarity Search & Caching

Queries are transformed into semantic vector embeddings via SentenceTransformer.  
These embeddings and their corresponding summaries are stored in ChromaDB.  
Incoming queries compare embeddings against the cache using cosine distance with a threshold (0.2).  
Matched cached answers are returned immediately, enabling efficient reuse and reducing unnecessary scraping.

---

## Web Scraping & Summarization

For uncached or novel queries:  
- Playwright automates web browser sessions to scrape the top 5 search results from DuckDuckGo, chosen for lighter anti-bot restrictions.  
- AI summarization models (Google Gemini API, OpenAI GPT, Hugging Face) distill the scraped content into concise, informative answers.  
- The processed summaries are cached for fast future retrieval.

---

## Engineering Decisions

- Opted for **simple heuristics** over complex AI models for query validation prioritizing speed and maintainability.  
- Chose **Playwright** over Selenium for faster, more reliable, and stealthier web scraping across multiple browsers.  
- Selected **DuckDuckGo** as the search engine for scraping to avoid restrictive bot blocks encountered on Google.  
- Integrated multiple AI summarization backends (Gemini, Hugging Face) to balance reliability and handle occasional download or API errors.  
- Used **ChromaDB** vector database to enable rich semantic search beyond keyword matching.

---

## Future Enhancements

- Integrate AI-based query validation for improved understanding without sacrificing latency.  
- Enhance summarization with multi-document context and user personalization.  
- Develop a polished frontend with more interactive and user-friendly features.  
- Expand scraping to multiple search engines and data sources for broader coverage.  
- Implement cache expiration, refresh policies, and incremental updates.

---

## Contributing

Contributions and issues are welcome! Please open issues or pull requests on the GitHub repository.

---

## License

This project is licensed under the MIT License.
