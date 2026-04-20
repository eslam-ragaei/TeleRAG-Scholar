import requests

class EmbeddingClient:

    def __init__(self):
        self.url = "http://10.255.255.254:9000/embed"

    def embed(self, text):
        res = requests.post(
            self.url,
            json={"text": text}
        )
        return res.json()["embedding"]

    def embed_query(self, text):
        return self.embed(text)

    def embed_documents(self, texts):
        return [self.embed(t) for t in texts]


# import torch
# import numpy as np
# from sentence_transformers import SentenceTransformer
# from langchain.embeddings.base import Embeddings


# class BgeM3Embeddings(Embeddings):
#     def __init__(self):
#         # Set seeds for deterministic behavior
#         torch.manual_seed(42)
#         np.random.seed(42)
#         self.model = SentenceTransformer("BAAI/bge-m3")
#         self.model.eval()  # Set to eval mode for consistency

#     def embed_documents(self, texts):
#         return self.model.encode(texts, normalize_embeddings=True, show_progress_bar=False).tolist()

#     def embed_query(self, text):
#         return self.model.encode(text, normalize_embeddings=True, show_progress_bar=False).tolist()