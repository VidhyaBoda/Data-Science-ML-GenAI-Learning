"""12 - Similarity ranking"""

documents = {
    "doc_1": 0.91,
    "doc_2": 0.72,
    "doc_3": 0.84,
    "doc_4": 0.63,
}

ranked = sorted(documents.items(), key=lambda item: item[1], reverse=True)

print("Documents ranked by similarity:")
for rank, (doc_id, score) in enumerate(ranked, 1):
    print(f"{rank}. {doc_id}: {score:.2f}")

print("\nIn a real system, these scores would come from an embedding/vector search method.")
