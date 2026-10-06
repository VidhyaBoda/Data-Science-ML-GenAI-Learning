"""20 - Mini vector database simulation

A small in-memory simulation for learning the core retrieval logic.
This is NOT a production vector database.
"""

import math

class MiniVectorDatabase:
    def __init__(self):
        self.records = {}

    def add(self, record_id, vector, metadata=None):
        self.records[record_id] = {
            "vector": vector,
            "metadata": metadata or {},
        }

    @staticmethod
    def cosine_similarity(a, b):
        if len(a) != len(b):
            raise ValueError("Vector dimensions must match.")

        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(y * y for y in b))

        if na == 0 or nb == 0:
            return 0.0

        return dot / (na * nb)

    def search(self, query_vector, top_k=3, metadata_filter=None):
        candidates = []

        for record_id, record in self.records.items():
            if metadata_filter:
                if any(
                    record["metadata"].get(key) != value
                    for key, value in metadata_filter.items()
                ):
                    continue

            score = self.cosine_similarity(query_vector, record["vector"])
            candidates.append((record_id, score, record["metadata"]))

        candidates.sort(key=lambda item: item[1], reverse=True)
        return candidates[:top_k]


db = MiniVectorDatabase()

db.add("doc_1", [0.9, 0.1, 0.0], {"department": "HR"})
db.add("doc_2", [0.2, 0.8, 0.1], {"department": "Finance"})
db.add("doc_3", [0.8, 0.2, 0.1], {"department": "HR"})
db.add("doc_4", [0.0, 0.1, 0.9], {"department": "IT"})

query = [1.0, 0.0, 0.0]

print("Top results:")
for result in db.search(query, top_k=3):
    print(result)

print("\nHR-only results:")
for result in db.search(
    query,
    top_k=3,
    metadata_filter={"department": "HR"},
):
    print(result)
