import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"Using Key: {api_key[:10]}...")

genai.configure(api_key=api_key)

candidates = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro",
    "gemini-1.5-pro-latest",
    "gemini-1.0-pro",
    "gemini-pro",
    "gemini-2.0-flash-exp",
    "gemini-2.0-flash-thinking-exp",
    "models/gemini-1.5-flash"
]

print("Searching for a working model...")
working_model = None

for model in candidates:
    try:
        print(f"Testing {model}...", end=" ")
        m = genai.GenerativeModel(model)
        m.generate_content("Hello")
        print("WORKS!")
        working_model = model
        break
    except Exception as e:
        err = str(e)
        if "429" in err:
            print("BUSY (429) - But Valid!")
            working_model = model # 429 means model exists
            break
        print("FAILED")

if working_model:
    print(f"FOUND WORKING MODEL: {working_model}")
    with open("backend/working_model.txt", "w") as f:
        f.write(working_model)
else:
    print("NO WORKING MODEL FOUND.")
