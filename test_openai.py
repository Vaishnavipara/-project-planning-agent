import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.models.list()
    print("✅ API key works! Available models:")
    for model in response.data:
        print("-", model.id)
except Exception as e:
    print("❌ API key test failed:", e)
