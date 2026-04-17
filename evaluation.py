from src.retrieval.query_data import search_db

"""
Build Evaluation logic to rank every question according to human intervention
"""
CHROMA_DB_PATH = "chroma_db"

test_questions = [
    "What statistical methods are commonly used to detect anomalies in 5G network KPIs?",
    "How does Isolation Forest work, and what are its advantages for network anomaly detection?",
    "What causes RRC connection failures in LTE networks?",
    "What evaluation metrics are used to measure anomaly detection performance in telecom papers?",
    "How can LLMs assist in telecom root cause analysis?"
]

def evaluate_query(query, k=10):
    query = query.strip()
    results = search_db(query=query, k=k)

    print("\n" + "="*60)
    print(f"QUERY: {query}")
    print("="*60)

    for i, (doc, score) in enumerate(results):
        print(f"\n--- Rank {i+1} ---")
        print(f"Score: {score:.2f}")
        print(f"Source: {doc.metadata['chunk_id']} with score: {score}")
        print("Content Preview:")
        print(doc.page_content)  # first 300 chars

    return results

def judge_relevance(results):
    """
    Manually inspect chunks and count relevant ones.
    You decide relevance based on printed content.
    """
    relevant = int(input("\nEnter number of relevant chunks (0-5): "))
    best_rank = int(input("Enter rank of BEST chunk (1-5): "))

    hit = 1 if relevant > 0 else 0

    return {
        "hit": hit,
        "relevant": relevant,
        "best_rank": best_rank
    }
    
    
def run_evaluation():
    results_table = []

    for i, q in enumerate(test_questions):
        print(f"\n\n Evaluating Q{i+1}")

        results = evaluate_query(q)

        eval_result = judge_relevance(results)

        results_table.append({
            "query": q,
            "hit": eval_result["hit"],
            "relevant": eval_result["relevant"],
            "best_rank": eval_result["best_rank"]
        })

    return results_table

def print_report(results_table):
    print("\n" + "="*80)
    print("FINAL EVALUATION REPORT")
    print("="*80)

    for i, row in enumerate(results_table):
        print(f"\nQ{i+1}: {row['query']}")
        print(f"Hit: {'YES' if row['hit'] else 'NO'}")
        print(f"Relevant Chunks: {row['relevant']}/5")
        print(f"Best Chunk Rank: {row['best_rank']}")
        
if __name__ == "__main__":
    results_table = run_evaluation()
    print_report(results_table)