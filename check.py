from dotenv import load_dotenv
import os
from google import genai

print("Loading .env...")
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", api_key is not None)
print("API key starts with:", api_key[:6] if api_key else None)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Say HELLO"
)

print("SUCCESS:", response.text)
