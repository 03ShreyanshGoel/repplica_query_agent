# import os
# from google import genai

# class GeminiClient:
#     def __init__(self):
#         self.api_key = os.getenv("GEMINI_API_KEY")
#         if not self.api_key:
#             raise ValueError("GEMINI_API_KEY not set in environment variables.")
#         self.client = genai.Client()

#     def summarize(self, text):
#         try:
#             response = self.client.models.generate_content(
#                 model="gemini-2.5-flash",
#                 contents=f"Please summarize the following text concisely:\n{text}"
#             )
#             return response.text.strip()
#         except Exception as e:
#             print(f"Gemini API error: {e}")
#             return None


import logging
import os
from google import genai

logger = logging.getLogger("gemini_client")

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            logger.error("Environment variable GEMINI_API_KEY not set")
            raise ValueError("GEMINI_API_KEY not set in environment variables.")
        logger.info("Initializing GeminiClient")
        self.client = genai.Client()

    def summarize(self, text):
        logger.info("Calling Gemini API to summarize text")
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Please summarize the following text concisely:\n{text}"
            )
            result = response.text.strip()
            logger.info("Gemini API summarization successful")
            return result
        except Exception as e:
            logger.error(f"Gemini API error: {e}", exc_info=True)
            return None
