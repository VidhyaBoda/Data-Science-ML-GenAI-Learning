"""18 - Retrieval evaluation"""

metrics = {
    "Precision@K": "How many retrieved items in the top K are relevant.",
    "Recall@K": "How many relevant items were retrieved within the top K.",
    "MRR": "Mean Reciprocal Rank; emphasizes the rank of the first relevant result.",
    "NDCG": "Measures ranking quality while considering graded relevance.",
}

for metric, meaning in metrics.items():
    print(f"{metric}: {meaning}")

print("\nEvaluate retrieval independently before blaming the LLM for poor RAG answers.")
