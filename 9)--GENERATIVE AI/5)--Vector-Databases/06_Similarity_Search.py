"""06 - Similarity search"""

import math

def cosine_similarity(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have equal dimensions.")
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)

query = [1, 0, 0]

documents = {
    "doc_A": [0.9, 0.1, 0.0],
    "doc_B": [0.1, 0.9, 0.0],
    "doc_C": [0.0, 0.1, 0.9],
}

for doc_id, vector in documents.items():
    score = cosine_similarity(query, vector)
    print(f"{doc_id}: {score:.4f}")
