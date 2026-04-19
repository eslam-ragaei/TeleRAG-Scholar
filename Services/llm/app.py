from fastapi import FastAPI
from pydantic import BaseModel

from client import LLMClient
from prompt import build_prompt

app = FastAPI(title="LLM Service")

llm = LLMClient()


class LLMRequest(BaseModel):
    query: str
    context: list


@app.get("/")
def health():
    return {"status": "LLM service running"}


@app.post("/generate")
def generate(request: LLMRequest):
    prompt = build_prompt(request.query, request.context)

    response = llm.generate(prompt)

    return {
        "response": response
    }