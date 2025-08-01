# from gemini_client import GeminiClient
# from transformers import pipeline

# # Initialize Gemini client once
# gemini_client = None
# try:
#     gemini_client = GeminiClient()
# except Exception as e:
#     print("Gemini client init failed:", e)

# # Fallback summarizer pipeline with HF if Gemini not available
# hf_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


# def summarize(text):
#     # Try Gemini summarization first
#     if gemini_client:
#         summary = gemini_client.summarize(text)
#         if summary:
#             return summary
#     # Else fallback to Hugging Face summarizer
#     return hf_summarizer(text, max_length=200, min_length=60, do_sample=False)[0]['summary_text']


import logging
from gemini_client import GeminiClient
from transformers import pipeline

logger = logging.getLogger("summarizer")

gemini_client = None
try:
    logger.info("Initializing Gemini client...")
    gemini_client = GeminiClient()
    logger.info("Gemini client initialized successfully.")
except Exception as e:
    logger.error(f"Gemini client init failed: {e}", exc_info=True)

logger.info("Initializing Hugging Face summarizer pipeline...")
hf_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
logger.info("Hugging Face summarizer pipeline ready.")

def summarize(text):
    logger.info("Starting text summarization...")
    if gemini_client:
        logger.info("Using Gemini client...")
        try:
            summary = gemini_client.summarize(text)
            if summary:
                logger.info("Gemini summarization successful.")
                return summary
            else:
                logger.warning("Gemini summarization returned empty result.")
        except Exception as e:
            logger.error(f"Error in Gemini summarization: {e}", exc_info=True)
    logger.info("Falling back to Hugging Face summarizer...")
    result = hf_summarizer(text, max_length=200, min_length=60, do_sample=False)
    logger.info("Hugging Face summarization completed.")
    return result[0]['summary_text']
