# import chromadb
# from sentence_transformers import SentenceTransformer
# import uuid

# client = chromadb.PersistentClient(path="./cache/chromadb")
# collection = client.get_or_create_collection("queries")

# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# SIMILARITY_THRESHOLD = 0.2  # Cosine distance threshold for similarity

# def embed(query):
#     return embedder.encode([query])[0].tolist()

# def search_similar(query):
#     query_emb = embed(query)
#     results = collection.query(query_embeddings=[query_emb], n_results=1)
#     # Defensive checks:
#     if (results and 
#         results.get('distances') and len(results['distances']) > 0 and
#         len(results['distances'][0]) > 0 and
#         len(results.get('metadatas', [])) > 0 and
#         len(results['metadatas'][0]) > 0):
        
#         if results['distances'][0][0] <= SIMILARITY_THRESHOLD:
#             return results['metadatas'][0][0].get('summary')
#     return None

# def add_to_memory(query, summary):
#     query_emb = embed(query)
#     unique_id = str(uuid.uuid4())  # generate a unique ID per entry
#     collection.add(
#         ids=[unique_id],  # <-- add this line
#         documents=[query],
#         embeddings=[query_emb],
#         metadatas=[{"query": query, "summary": summary}]
#     )



import logging
import chromadb
from sentence_transformers import SentenceTransformer
import uuid

logger = logging.getLogger("memory")

client = chromadb.PersistentClient(path="./cache/chromadb")
collection = client.get_or_create_collection("queries")

embedder = SentenceTransformer("all-MiniLM-L6-v2")

SIMILARITY_THRESHOLD = 0.2  # Cosine distance threshold

def embed(query):
    logger.debug(f"Embedding query: {query!r}")
    return embedder.encode([query])[0].tolist()

def search_similar(query):
    logger.info(f"Searching for similar past queries for: {query}")
    query_emb = embed(query)
    results = collection.query(query_embeddings=[query_emb], n_results=1)
    if (results and results.get('distances') and len(results['distances']) > 0 and 
        len(results['distances'][0]) > 0 and len(results.get('metadatas', [])) > 0 and 
        len(results['metadatas'][0]) > 0):
        similarity = results['distances'][0][0]
        logger.debug(f"Found similarity: {similarity}")
        if similarity <= SIMILARITY_THRESHOLD:
            summary = results['metadatas'][0][0].get('summary')
            logger.info("Similar summary found in cache.")
            return summary
    logger.info("No similar summary found.")
    return None

def add_to_memory(query, summary):
    logger.info("Adding query + summary to cache memory.")
    query_emb = embed(query)
    unique_id = str(uuid.uuid4())
    collection.add(
        ids=[unique_id],
        documents=[query],
        embeddings=[query_emb],
        metadatas=[{"query": query, "summary": summary}]
    )
    logger.info("Entry added to cache.")
