import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from fastapi import FastAPI
from pydantic import BaseModel

from services.retrieval.retriever import Retriever

app = FastAPI(title="Retrieval Service")

retriever = Retriever()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def health():
    return {"status": "Retrieval service running"}


@app.post("/retrieve")
def retrieve(request: QueryRequest):
    results = retriever.retrieve(request.query)
    return {"chunks": results} #doc type or class instance