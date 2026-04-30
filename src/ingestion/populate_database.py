import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
from src.embeddings.get_embedding import BgeM3Embeddings
from src.ingestion.loader import load_documents
from src.ingestion.chunking import chunk_documents
from langchain_chroma import Chroma
import os
import shutil
from tqdm import tqdm


DATA_PATH = "data/"
CHROMA_DB_PATH = "chroma_db"

def clear_database():
    """
    Delete existing ChromaDB to avoid duplicate data
    
    """
    if os.path.exists(CHROMA_DB_PATH):
        shutil.rmtree(CHROMA_DB_PATH)
        print("Old database cleared.")
        
def populate_database():
    
    """
    Create the Vector of embeddings from my data
    """
    
    # Load files into documents
    documents = load_documents(data_path=DATA_PATH)
    
    #Chunk the documents with more precise text segments
    chunks = chunk_documents(documents=documents, chunk_size=1200, chunk_overlap=200)
    
    #Create embedding instance
    embedder = BgeM3Embeddings()
    
    #Create vector store database from documents directly
    db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedder,
        collection_metadata={"hnsw:space": "cosine"}
    )
    
    batch_size = 64

    for i in tqdm(range(0, len(chunks), batch_size)):
        batch = chunks[i:i+batch_size]
        db.add_documents(batch)

    
    print(f"Database created with {len(chunks)} chunks.")

if __name__ == "__main__":
    
    print("Use the UI for interactive usage")
    
    if os.path.exists(CHROMA_DB_PATH):
        
        answer = input("Do you need to clear the database : (y/n)\nif yes it will be cleared and populate the new one\nyour answer: ").strip().lower()
        
        if answer in ['yes' , 'y']:
            
            clear_database()
            populate_database()
            
        else:
            print("Keep old one.")
            
    else:
        print("No database found")
        populate_database()