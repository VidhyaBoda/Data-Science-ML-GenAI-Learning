"""14 - Embedding model considerations"""

factors = [
    "Semantic quality",
    "Language coverage",
    "Embedding dimension",
    "Latency",
    "Cost",
    "Maximum input length",
    "Domain suitability",
    "Availability of local/self-hosted deployment",
    "Similarity metric compatibility",
]

print("When selecting an embedding model, evaluate:")
for factor in factors:
    print("-", factor)

print("\nDo not choose a model only because it has a larger dimension.")
