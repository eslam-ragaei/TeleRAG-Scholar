import requests


class RetrievalClient:
    def __init__(self):
        self.url = "http://retrieval-service:8001/retrieve"

    def retrieve(self, query):
        response = requests.post(self.url, json={"query": query})
        return response.json()["chunks"]


class LLMClient:
    def __init__(self):
        self.url = "http://llm-service:8002/generate"

    def generate(self, query, context):
        response = requests.post(self.url, json={
            "query": query,
            "context": context
        })
        return response.json()