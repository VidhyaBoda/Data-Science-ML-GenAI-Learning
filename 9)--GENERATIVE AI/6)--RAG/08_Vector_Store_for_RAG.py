"""
08 - Vector Store for RAG
Minimal in-memory vector store.
"""

class VectorStore:
    def __init__(self):
        self.records = []

    def add(self, doc_id, vector, text, metadata=None):
        self.records.append({
            "id": doc_id,
            "vector": vector,
            "text": text,
            "metadata": metadata or {}
        })

    def count(self):
        return len(self.records)

store = VectorStore()
store.add("d1", [0.1, 0.2, 0.3], "RAG retrieves relevant context.", {"source": "rag.md"})
store.add("d2", [0.4, 0.5, 0.6], "Embeddings represent semantic meaning.", {"source": "embeddings.md"})

print("Stored records:", store.count())
for record in store.records:
    print(record)
