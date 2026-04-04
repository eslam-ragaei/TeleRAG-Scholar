import ollama
from langchain.embeddings.base import Embeddings

class BGEM3Embeddings(Embeddings):
    
    """
    Custom embedding class using Ollama bge-m3 model.
    Compatible with LangChain and ChromaDB.
    
    """
    
    def __init__(self , model_name = "bge-m3" , base_url = "http://localhost:11434" , temperature = 0.0):
        """
        initalize BGE-M3 embedding model from Ollama.
        
        Args:
            model_name (str): Name of the Ollama model to use for embeddings.
            base_url (str): Base URL for the Ollama API.
            temperature (float): Temperature setting for the embedding model.
        
        """
        
        self.model = model_name
        self.base_url = base_url
        self.temperature = temperature
        
    def embed_documents (self , texts):
        
        """
        Embed a list of documents.
        
        Args:
            texts (List[str]): List of chunk texts to embed.
            
        Returns:
            List[List[float]]: List of embedding vectors for each chunk.            
        
        """
        
        embeddings = []
        
        for text in texts:
            
            reponse = ollama.embeddings (
                model=self.model,
                prompt=text
            )
            
            embeddings.append(reponse['embedding'])
            
        return embeddings
            
    def embed_query(self, text):
        
        """
        Embed the question query
        
        Args:
        Question (str): The question query to embed.
        
        Returns:
        List[float]: Embedding vector for the question query.
        
        """
        
        
        reponse = ollama.embeddings (
                model=self.model,
                prompt=text
            )
        return reponse['embedding']