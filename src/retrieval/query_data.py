import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from langchain_chroma import Chroma
from src.embeddings.get_embedding import BgeM3Embeddings
from src.retrieval.reranker import Reranker


CHROMA_DB_PATH = "chroma_db"


def get_db(CHROMA_DB_PATH = CHROMA_DB_PATH):
    embedder = BgeM3Embeddings()
    db = Chroma(
        persist_directory=CHROMA_DB_PATH , 
        embedding_function=embedder,
        collection_metadata={"hnsw:space": "cosine"} 
    )
    
    return db

def search_db(query , k=10):
    
    """
    Return the query similarities answers
    
    Args:
        Query (str) : you Question
        
    Returns:
        results ([(Document, distance), (Document, distance), ...]) : your similar answer and its l2 distance
    """
    
    
    db = get_db()
    
    reranker = Reranker()

# Step 1: retrieve more candidates
    results = db.similarity_search_with_score(query, k=k)

    # Step 2: rerank
    reranked_docs = reranker.rerank(query, results)

    # Step 3: take top 5
    results = reranked_docs[:5]
    
    return results

def build_context(results):
    
    context = ""
    sources = []
    
    for doc, score in results:
        
        context += doc.page_content + "\n\n"
        sources.append(f"{doc.metadata["chunk_id"]} with score: {score}")
        
    return context ,sources



    
    