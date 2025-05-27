# type:ignore
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def request_ai_review(prompt):
    """Request AI review with strict prompt."""
    client = genai.Client(api_key=GEMINI_API_KEY)
    print("\n🤖 Requesting AI review with detailed changed lines...")
    response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    # print("\n🔍 AI Review Result:\n")
    # print(response.text)
    print("\n✅ Review Completed.\n")
    return response.text
