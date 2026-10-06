"""05 - Cosine similarity"""

import math

def cosine_similarity(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")

    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    return dot / (norm_a * norm_b)


v1 = [1, 2, 3]
v2 = [1, 2, 3]
v3 = [-1, -2, -3]

print("Similarity(v1, v2):", cosine_similarity(v1, v2))
print("Similarity(v1, v3):", cosine_similarity(v1, v3))

print("\nCosine similarity measures the angle between vectors.")
