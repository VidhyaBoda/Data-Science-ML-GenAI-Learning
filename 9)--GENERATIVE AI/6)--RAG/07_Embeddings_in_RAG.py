"""
07 - Embeddings in RAG
Convert documents and queries into vectors for semantic retrieval.
"""

documents = {
    "doc_1": [0.90, 0.10, 0.20],
    "doc_2": [0.10, 0.90, 0.20],
    "doc_3": [0.70, 0.20, 0.30]
}

query_vector = [0.85, 0.15, 0.20]

print("Query vector:", query_vector)
print("\nDocument vectors:")
for doc_id, vector in documents.items():
    print(doc_id, vector)

print("\nRAG uses similarity between the query vector and document vectors.")
