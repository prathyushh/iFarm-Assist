import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

def generate_rag_response(query: str, context: str):
    if not GOOGLE_API_KEY:
        return "Error: GOOGLE_API_KEY not configured"
    
    # Retry configuration
    retries = 1
    delay = 60 # seconds

    try:
        print("DEBUG: Initializing Gemini Model (gemini-flash-latest)...")
        model = genai.GenerativeModel("gemini-flash-latest")
        
        prompt = f"""You are iFarmAssist, an expert agricultural AI assistant for farmers in Kerala.
Use the following pieces of context to answer the user's question.

FORMATTING RULES:
1. Use **Bold** for headers and key terms.
2. Use *Bullet points* for lists.
3. Use TABLES (Markdown format) for comparisons or structured data.
4. Keep paragraphs short and readable.
5. Add emojis (🌿, 🚜, 💧) to make it friendly.

If the answer is not in the context, say "I don't have enough information to answer that based on the provided documents" and suggest consulting an expert.
Answer in simple, clear language. If asked in Malayalam, reply in Malayalam (transliterate if needed or use script).

Context:
{context}

Question: 
{query}
"""
        # Retry Loop
        for attempt in range(retries + 1):
            try:
                print(f"DEBUG: Sending request to Gemini (Attempt {attempt+1})...")
                response = model.generate_content(prompt)
                print("DEBUG: Received response from Gemini.")
                return response.text
            except Exception as e:
                error_str = str(e)
                if "429" in error_str and attempt < retries:
                    print(f"WARNING: Rate Limit Hit (429). Retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                else:
                    # If other error or retries exhausted, re-raise to outer block
                    raise e

    except Exception as e:
        print(f"CRITICAL GEMINI ERROR: {e}")
        error_str = str(e)
        if "429" in error_str or "quota" in error_str.lower():
            return "⚠️ I am receiving high traffic right now (Free Tier Limit). Please wait 60 seconds and try again! 🙏"
        return f"AI Error: {error_str}"
