"""07 - Dot product"""

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")
    return sum(x * y for x, y in zip(a, b))


v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("Dot product:", dot_product(v1, v2))
print()
print("Dot product is frequently used in vector similarity calculations.")
print("Its interpretation depends on vector magnitude and normalization.")
