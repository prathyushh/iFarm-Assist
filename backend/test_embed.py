from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

try:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
    res = embeddings.embed_query("This is a test.")
    print(f"Success! Embedding length: {len(res)}")
except Exception as e:
    print(f"Error: {e}")
