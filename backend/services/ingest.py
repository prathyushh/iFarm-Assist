import os
try:
    from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma
except ImportError as e:
    print(f"Import Error: {e}")
    raise e

from dotenv import load_dotenv

load_dotenv()

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chroma_db")

def ingest_docs():
    if not os.path.exists(DATA_PATH):
        print(f"Data directory not found: {DATA_PATH}")
        return

    print(f"Data Path: {DATA_PATH}")
    print("Loading PDFs...")
    try:
        # Load all PDFs
        loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
    except Exception as e:
        print(f"Error loading PDFs: {e}")
        return

    if not documents:
        print("No documents found in data folder.")
        return

    print(f"Loaded {len(documents)} document pages.")

    print("Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")

    print("Embedding and storing in ChromaDB (using local model: all-MiniLM-L6-v2)...")
    try:
        # Use local embeddings to avoid API limits
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Create Vector Store
        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=DB_PATH
        )
        print("Ingestion complete! Knowledge base updated locally.")
    except Exception as e:
        print(f"Error creating vector store: {e}")

if __name__ == "__main__":
    ingest_docs()
