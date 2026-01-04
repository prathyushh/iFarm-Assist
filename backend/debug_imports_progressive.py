import sys

print("1. Importing os/sys...")
import os

print("2. Importing python-dotenv...")
from dotenv import load_dotenv
load_dotenv()

print("3. Importing sqlalchemy...")
from sqlalchemy import create_engine

print("4. Importing google-generativeai...")
import google.generativeai

print("5. Importing langchain-google-genai...")
from langchain_google_genai import ChatGoogleGenerativeAI

print("6. Importing chromadb (Common Failure Point)...")
import chromadb

print("7. Importing sentence-transformers (Heavy)...")
from sentence_transformers import SentenceTransformer

print("8. Importing langchain-huggingface...")
from langchain_huggingface import HuggingFaceEmbeddings

print("ALL IMPORTS OK")
