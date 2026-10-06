"""
19 - RAG Evaluation
Basic retrieval metrics.
"""

relevant = {"d1", "d3", "d5"}
retrieved = ["d1", "d2", "d3"]

hits = len(set(retrieved) & relevant)
precision_at_k = hits / len(retrieved)
recall = hits / len(relevant)

print(f"Precision@{len(retrieved)}: {precision_at_k:.2f}")
print(f"Recall: {recall:.2f}")

print("\nProduction evaluation should separately measure:")
print("- retrieval quality")
print("- answer faithfulness")
print("- answer relevance")
print("- latency")
print("- cost")
