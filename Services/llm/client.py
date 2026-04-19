import requests


class LLMClient:
    def __init__(self):
        self.url = "http://ollama:11434/api/generate"
        self.model = "mistral"

    def generate(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]