import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"Using Key: {api_key[:10]}...")
genai.configure(api_key=api_key)

models_to_test = ["gemini-1.5-flash", "gemini-2.0-flash-exp", "gemini-1.5-flash-latest"]

print("\n--- Starting Latency Test ---\n")

for model_name in models_to_test:
    print(f"Testing: {model_name}")
    start_time = time.time()
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Reply with 'Pong'", request_options={"timeout": 10})
        duration = time.time() - start_time
        print(f"SUCCESS: {duration:.2f}s | Response: {response.text.strip()}")
    except Exception as e:
        duration = time.time() - start_time
        print(f"FAILED: {duration:.2f}s | Error: {str(e)[:100]}...")
    print("-" * 30)
