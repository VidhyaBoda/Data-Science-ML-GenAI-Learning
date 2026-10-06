"""12 - Distance metrics"""

metrics = {
    "Cosine similarity": "Measures orientation/angle between vectors.",
    "Dot product": "Combines vector alignment and magnitude.",
    "Euclidean distance": "Measures geometric distance between points.",
}

for name, description in metrics.items():
    print(f"{name}: {description}")

print("\nThe metric should be compatible with the embedding model and retrieval design.")
