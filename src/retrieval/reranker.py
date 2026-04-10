from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(self):
        self.model = CrossEncoder("BAAI/bge-reranker-base")

    def rerank(self, query, docs):
        pairs = [(query, doc.page_content) for doc, _ in docs]

        scores = self.model.predict(pairs)

        # Combine docs with new scores
        reranked = list(zip(docs, scores))

        # Sort by reranker score
        reranked = sorted(reranked, key=lambda x: x[1], reverse=True)

        return [item[0] for item in reranked]