"""06 - Euclidean distance"""

import math

def euclidean_distance(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")

    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


v1 = [1, 2]
v2 = [2, 4]

print("Euclidean distance:", euclidean_distance(v1, v2))
print("\nSmaller distance means the points are closer in Euclidean space.")
