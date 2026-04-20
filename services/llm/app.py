import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from fastapi import FastAPI
from pydantic import BaseModel

from services.llm.client import LLMClient
from services.llm.prompt import build_prompt

app = FastAPI(title="LLM Service")

llm = LLMClient()


class LLMRequest(BaseModel):
    query: str
    context: dict


@app.get("/")
def health():
    return {"status": "LLM service running"}


@app.post("/generate")
def generate(request: LLMRequest):
    prompt = build_prompt(request.query, request.context)
    print("prompt")
    response = llm.generate(prompt)

    return response