import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from fastapi import FastAPI
from services.api.client import RetrievalClient, LLMClient

app = FastAPI(title="TeleRAG API Gateway")

retrieval_client = RetrievalClient()
llm_client = LLMClient()


@app.get("/")
def health():
    return {"status": "API Gateway is running"}


@app.post("/query")
def query(payload: dict):
    question = payload.get("question")

    # 1️⃣ Get relevant chunks
    retrieved_docs = retrieval_client.retrieve(question)

    # 2️⃣ Send to LLM
    answer = llm_client.generate(question, retrieved_docs)
    
    return {
        "question": question,
        "docs": retrieved_docs["chunks"],
        "answer": answer
    }
    
