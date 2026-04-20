import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from langchain_chroma import Chroma
from services.retrieval.RemoteBGEEmbeddings import RemoteBGEEmbeddings


CHROMA_DB_PATH = os.path.join(project_root, "chroma_db")


def get_vector_db(CHROMA_DB_PATH = CHROMA_DB_PATH):
    embedder = RemoteBGEEmbeddings()
    db = Chroma(
        persist_directory=CHROMA_DB_PATH , 
        embedding_function=embedder,
        collection_metadata={"hnsw:space": "cosine"} 
    )
    
    return db