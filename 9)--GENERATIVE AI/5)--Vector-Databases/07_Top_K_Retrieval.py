"""07 - Top-K retrieval"""

results = [
    ("doc_A", 0.92),
    ("doc_B", 0.84),
    ("doc_C", 0.71),
    ("doc_D", 0.66),
]

k = 2
top_k = sorted(results, key=lambda item: item[1], reverse=True)[:k]

print(f"Top-{k} results:")
for rank, (doc_id, score) in enumerate(top_k, 1):
    print(f"{rank}. {doc_id} -> {score:.2f}")

print("\nTop-K is a retrieval parameter, not a universal constant.")
