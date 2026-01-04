import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found.")
    exit()

genai.configure(api_key=api_key)

print("Listing available models...")
try:
    with open("backend/available_models.txt", "w") as f:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
                f.write(f"{m.name}\n")
    print("Models listed to backend/available_models.txt")
except Exception as e:
    print(f"Error listing models: {e}")
