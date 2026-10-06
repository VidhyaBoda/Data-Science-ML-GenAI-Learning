"""
11 - Top-K Retrieval
Retrieve the highest-scoring documents.
"""

results = [
    ("doc_1", 0.94),
    ("doc_2", 0.89),
    ("doc_3", 0.84),
    ("doc_4", 0.61),
    ("doc_5", 0.40)
]

k = 3
top_k = sorted(results, key=lambda x: x[1], reverse=True)[:k]

print(f"Top {k} results:")
for doc_id, score in top_k:
    print(doc_id, round(score, 4))
