from langchain.embeddings.base import Embeddings
from shared.get_embedding import EmbeddingClient

class RemoteBGEEmbeddings(Embeddings):

    def __init__(self):
        self.client = EmbeddingClient()

    def embed_documents(self, texts):
        return self.client.embed_documents(texts)

    def embed_query(self, text):
        return self.client.embed_query(text)