import os
try:
    from langchain_community.vectorstores import Chroma
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError as e:
    raise e

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chroma_db")

# Lazy load embeddings
_embeddings = None

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        print("Loading Embeddings Model (Lazy)...")
        _embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return _embeddings

def get_retriever():
    if not os.path.exists(DB_PATH):
        return None
    
    vector_db = Chroma(persist_directory=DB_PATH, embedding_function=get_embeddings())
    return vector_db.as_retriever(search_kwargs={"k": 3})

def search_knowledge_base(query: str):
    retriever = get_retriever()
    if not retriever:
        return "Knowledge Base Not Initialized. Please run ingestion script."
    
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context
