# 14 - Embeddings and Vector Stores

documents = [
    {"text": "RAG uses retrieval to provide context.", "vector": [0.9, 0.1]},
    {"text": "Embeddings convert text into vectors.", "vector": [0.2, 0.8]}
]

query_vector = [0.85, 0.15]

print("Query vector:", query_vector)
for doc in documents:
    print(doc)
