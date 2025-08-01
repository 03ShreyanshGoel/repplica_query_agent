# uvicorn app:app --reload --host 0.0.0.0 --port 8000


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# from memory import search_similar, add_to_memory
# from searcher import get_search_results, extract_text_from_url
# from summarizer import summarize
# from validator import is_query_valid

# app = FastAPI()

# # Allow CORS from frontend localhost:3000
# origins = ["http://localhost:3000"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class QueryRequest(BaseModel):
#     query: str

# @app.post("/query")
# async def handle_query(req: QueryRequest):
#     query = req.query.strip()
#     if not query:
#         raise HTTPException(status_code=400, detail="Query cannot be empty")

#     if not is_query_valid(query):
#         raise HTTPException(status_code=400, detail="Invalid query")

#     cached_summary = search_similar(query)
#     if cached_summary:
#         return {"summary": cached_summary}

#     urls = urls = await get_search_results(query)
#     if not urls:
#         return {"summary": "No search results found."}

#     contents = []
#     for url in urls:
#         text = extract_text_from_url(url)
#         if text:
#             contents.append(text)

#     if not contents:
#         return  {"summary": "Could not extract content from search results."}

#     page_summaries = [summarize(c) for c in contents if c]
#     combined_text = "\n\n".join(page_summaries)

#     if not combined_text.strip():
#         return {"summary": "Could not generate summary."}

#     combined_summary = summarize(combined_text)

#     add_to_memory(query, combined_summary)

#     return {"summary": combined_summary}

# uvicorn app:app --host 0.0.0.0 --port 8000  --log-level debug


import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from memory import search_similar, add_to_memory
from searcher import get_search_results, extract_text_from_url
from summarizer import summarize
from validator import is_query_valid

logger = logging.getLogger("app")

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class QueryRequest(BaseModel):
    query: str

@app.on_event("startup")
def startup_event():
    logger.info("Starting FastAPI application...")

@app.post("/query")
async def handle_query(req: QueryRequest):
    query = req.query.strip()
    logger.info(f"Received query: {query!r}")

    if not query:
        logger.warning("Empty query received")
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    if not is_query_valid(query):
        logger.warning(f"Invalid query: {query!r}")
        raise HTTPException(status_code=400, detail="Invalid query")

    cached_summary = search_similar(query)
    if cached_summary:
        logger.info("Found cached summary in memory")
        return {"summary": cached_summary}

    logger.info("Cache miss, fetching search results...")
    urls = await get_search_results(query)
    logger.info(f"Found {len(urls)} URLs for query")

    if not urls:
        logger.info("No search results found.")
        return {"summary": "No search results found."}

    contents = []
    for url in urls:
        text = extract_text_from_url(url)
        if text:
            contents.append(text)
        else:
            logger.warning(f"No text extracted from URL: {url}")

    if not contents:
        logger.warning("Could not extract content from search results")
        return {"summary": "Could not extract content from search results."}

    page_summaries = [summarize(c) for c in contents if c]
    combined_text = "\n\n".join(page_summaries)

    if not combined_text.strip():
        logger.warning("Could not generate combined summary from page summaries")
        return {"summary": "Could not generate summary."}

    combined_summary = summarize(combined_text)
    logger.info("Generated combined summary")

    add_to_memory(query, combined_summary)
    logger.info("Added summary to memory")

    return {"summary": combined_summary}
