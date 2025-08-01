from gemini_client import GeminiClient
from transformers import pipeline

# Initialize Gemini client once
gemini_client = None
try:
    gemini_client = GeminiClient()
except Exception as e:
    print("Gemini client init failed:", e)

# Fallback summarizer pipeline with HF if Gemini not available
hf_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize(text):
    # Try Gemini summarization first
    if gemini_client:
        summary = gemini_client.summarize(text)
        if summary:
            return summary
    # Else fallback to Hugging Face summarizer
    return hf_summarizer(text, max_length=200, min_length=60, do_sample=False)[0]['summary_text']
