try:
    print("Importing FastAPI...")
    from fastapi import FastAPI
    print("Importing SQLAlchemy...")
    from sqlalchemy import create_engine
    print("Importing Pydantic...")
    from pydantic import BaseModel
    print("Importing LangChain HuggingFace...")
    from langchain_huggingface import HuggingFaceEmbeddings
    print("Importing ChromaDB...")
    import chromadb
    print("Importing Google GenAI...")
    import google.generativeai
    print("ALL IMPORTS SUCCESSFUL")
except Exception as e:
    print(f"IMPORT FAILED: {e}")
