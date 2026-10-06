"""
10 - Similarity Retrieval
A simple cosine-similarity retriever.
"""

import math

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0

query = [1, 0, 0]
documents = {
    "doc_a": [0.9, 0.1, 0],
    "doc_b": [0.1, 0.9, 0],
    "doc_c": [0.8, 0.2, 0]
}

scores = []
for doc_id, vector in documents.items():
    score = cosine_similarity(query, vector)
    scores.append((doc_id, score))

for doc_id, score in sorted(scores, key=lambda x: x[1], reverse=True):
    print(f"{doc_id}: {score:.4f}")
