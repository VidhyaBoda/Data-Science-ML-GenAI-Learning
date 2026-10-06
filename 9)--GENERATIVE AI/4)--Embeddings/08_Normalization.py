"""08 - Vector normalization"""

import math

def l2_normalize(vector):
    norm = math.sqrt(sum(x * x for x in vector))
    if norm == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return [x / norm for x in vector]


vector = [3, 4]
normalized = l2_normalize(vector)

print("Original:", vector)
print("Normalized:", normalized)

length = math.sqrt(sum(x * x for x in normalized))
print("Normalized L2 length:", length)
