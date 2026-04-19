from fastapi import FastAPI
from pydantic import BaseModel

from retriever import Retriever

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
    return {"chunks": results}