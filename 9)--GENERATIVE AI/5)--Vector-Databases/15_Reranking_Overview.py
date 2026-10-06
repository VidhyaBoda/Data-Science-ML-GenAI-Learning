"""15 - Reranking overview"""

print("A common retrieval architecture:")
print()
print("1. Vector search retrieves a larger candidate set.")
print("2. A reranker scores the candidates more precisely.")
print("3. The application keeps the best final results.")
print()
print("Example:")
print("Top-50 candidate chunks -> reranker -> top-5 final chunks")
print()
print("Reranking can improve precision at the cost of additional latency/compute.")
