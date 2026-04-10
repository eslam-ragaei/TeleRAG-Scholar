from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

class BgeM3Embeddings(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-m3")

    def embed_documents(self, texts):
        return self.model.encode(texts, normalize_embeddings=True).tolist()

    def embed_query(self, text):
        return self.model.encode(text, normalize_embeddings=True).tolist()