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

<img width="980" height="681" alt="diagram-export-1-8-2025-10_43_51-pm" src="https://github.com/user-attachments/assets/63a29da0-184f-4d54-bc95-6945aba9f0e3" />


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
- **AI Summarization:** Google Gemini API, Hugging Face models for diverse summarization options  
- **Utilities:** UUID for unique caching keys, Python logging for traceability  

---

## Installation

### Prerequisites

- Python 3.10+ for FastAPI backend  
- Node.js and npm/yarn for React frontend and Playwright dependencies  
- Access to AI API keys (Gemini, OpenAI, Hugging Face) configured via environment variables  

### Setup Instructions

