from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(self):
        self.model = CrossEncoder("BAAI/bge-reranker-base")

    def rerank(self, query, docs):
        pairs = [(query, doc.page_content) for doc, _ in docs]

        scores = self.model.predict(pairs)

        # Combine docs with new scores and index for tie-breaking
        reranked = [(docs[i], scores[i], i) for i in range(len(docs))]

        # Sort by reranker score (descending), then by original index (ascending) for deterministic tie-breaking
        reranked = sorted(reranked, key=lambda x: (-x[1], x[2]))

        return [item[0] for item in reranked]