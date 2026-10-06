"""15 - Embedding limitations"""

limitations = [
    "Similar vectors do not guarantee factual correctness.",
    "Domain-specific terminology may require a suitable embedding model.",
    "Chunking choices strongly affect retrieval quality.",
    "A single vector may compress away important details.",
    "Similarity scores are model- and data-dependent.",
    "Multilingual performance varies across models.",
]

print("Important limitations:")
for item in limitations:
    print("-", item)
