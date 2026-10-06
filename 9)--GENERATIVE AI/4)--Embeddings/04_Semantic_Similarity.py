"""04 - Semantic similarity"""

sentences = [
    "The car is fast.",
    "The automobile has high speed.",
    "I cooked vegetable soup."
]

print("Embeddings can represent semantic relationships.")
print()
for sentence in sentences:
    print("-", sentence)

print("\nConceptual expectation:")
print("The first two sentences should generally be more semantically related")
print("than either one is to the soup sentence.")
