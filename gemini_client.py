import os
from google import genai

class GeminiClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set in environment variables.")
        self.client = genai.Client()

    def summarize(self, text):
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Please summarize the following text concisely:\n{text}"
            )
            return response.text.strip()
        except Exception as e:
            print(f"Gemini API error: {e}")
            return None
