import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

candidates = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro",
    "gemini-1.5-pro-latest",
    "gemini-1.0-pro",
    "gemini-pro",
    "gemini-2.0-flash-exp"
]

print("Testing Model Availability...")
for model in candidates:
    try:
        print(f"Testing {model}...", end=" ")
        m = genai.GenerativeModel(model)
        response = m.generate_content("Hello")
        print(f"SUCCESS! -> {model}")
        # Save the working model to a file so we can read it
        with open("backend/valid_model.txt", "w") as f:
            f.write(model)
        break
    except Exception as e:
        print(f"FAILED ({str(e)[:50]}...)")
