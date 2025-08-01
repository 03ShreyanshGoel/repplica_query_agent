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

This project implements an intelligent web browser query agent designed for **Ripplica**, led by CEO Bhavesh. The agent intelligently validates user queries, efficiently reuses cached answers for semantically similar queries, scrapes new data using Playwright when needed, and summarizes web results using state-of-the-art AI models. The result is a fast, user-friendly search assistant that balances performance, maintainability, and accuracy.

---

## Features

- Lightweight and fast query validation using simple heuristics  
- Semantic similarity search with sentence embeddings stored in ChromaDB  
- Automated web scraping of top search results using Playwright  
- AI-powered summarization of scraped content  
- Caching of query and summary pairs for instant responses on repeated queries  
- Modular architecture enabling easy maintenance and future improvements  

---

## Architecture & Workflow

<img width="980" height="681" alt="diagram-export-1-8-2025-10_43_51-pm" src="https://github.com/user-attachments/assets/14f8b2ad-4cfa-499b-a009-a1744d8ac69c" />

*Figure: System flow from query input through validation, caching, scraping, summarization, and response*

The system follows this high-level flow:

1. User inputs a query  
2. System validates the query with heuristics  
3. If valid, searches cache for semantically similar queries  
4. Returns cached summary if similarity is above threshold  
5. If no cached answer, runs Playwright to scrape top 5 web results  
6. Uses AI model to summarize content  
7. Stores new query + summary in cache  
8. Returns concise summary to user

   


---

## Technology Stack

- **Backend:** Python (for API and processing)  
- **Web Scraping:** Playwright  
- **Semantic Search:** SentenceTransformers (all-MiniLM-L6-v2) embeddings + ChromaDB vector database  
- **AI Summarization:** OpenAI GPT, Google Gemini API, and Hugging Face models  
- **Frontend:** (Optional) React.js or CLI client  
- **Other:** UUID for unique cache keys, logging for traceability  

---

## Installation

### Prerequisites

- Python 3.8+  
- Node.js (if running frontend or for Playwright)  

### Setup

