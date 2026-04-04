import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from langchain_chroma import Chroma
from src.embeddings.get_embedding import BGEM3Embeddings
from langchain_ollama import OllamaLLM


CHROMA_DB_PATH = "chroma_db"


def get_db(CHROMA_DB_PATH = CHROMA_DB_PATH):
    embedder = BGEM3Embeddings()
    db = Chroma(
        persist_directory=CHROMA_DB_PATH , 
        embedding_function=embedder
    )
    
    return db

def search_db(query , k=5):
    
    """
    Return the query similtaties answers
    
    Args:
        Query (str) : you Question
        
    Returns:
        results ([(Document, disatnce), (Document, disatnce), ...]) : your similar answer and its l2 distance
    """
    
    
    db = get_db()
    results = db.similarity_search_with_score(query=query , k=k)
    
    return results

def build_context(results):
    
    context = ""
    sources = []
    
    for doc, score in results:
        
        context += doc.page_content + "\n\n"
        sources.append(f"{doc.metadata["chunk_id"]} with score: {score}")
        
    return context ,sources



    
    