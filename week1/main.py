
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Create Gemini client
from google.genai import types

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=30000)
)

print("Sending request to Gemini...", flush=True)

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Display response
print("\nLLM Response:")
print(response.text)
