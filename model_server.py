from fastapi import FastAPI
from sentence_transformers import SentenceTransformer, CrossEncoder
import torch
import numpy as np

app = FastAPI()

# Load models once (important)
torch.manual_seed(42)
np.random.seed(42)
embedding_model = SentenceTransformer("BAAI/bge-m3")
embedding_model.eval()
reranker_model = CrossEncoder("BAAI/bge-reranker-base")


# -------------------------
# Embeddings endpoint
# -------------------------
@app.post("/embed")
def embed(data: dict):

    text = data["text"]
    vector = embedding_model.encode(text).tolist()
    return {"embedding": vector}


# -------------------------
# Reranker endpoint
# -------------------------
@app.post("/rerank")
def rerank(data: dict):
    query = data["query"]
    docs = data["docs"]

    pairs = [(query, d["content"]) for d in docs]
    scores = reranker_model.predict(pairs)

    results = []
    for i in range(len(docs)):
        results.append({
            "doc": docs[i],
            "score": float(scores[i]),
            "index": i
        })

    results.sort(key=lambda x: (-x["score"], x["index"]))

    return {"results": results}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "model_server:app",
        host="0.0.0.0",
        port=9000,
        reload=True
    )