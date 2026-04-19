from db import get_vector_db
from reranker import Reranker


class Retriever:
    def __init__(self):
        self.db = get_vector_db()
        self.reranker = Reranker()

    def retrieve(self, query):
        # Step 1: Retrieve candidates (top 10)
        docs = self.db.similarity_search_with_score(query, k=10)

        # Step 2: Rerank
        reranked = self.reranker.rerank(query, docs)

        # Step 3: Take top 5
        final_docs = reranked[:5]

        # Step 4: Format response
        results = []
        for doc, score in final_docs:
            results.append({
                "content": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            })

        return results
    
