"""04 - Vectors, metadata and collections"""

record = {
    "id": "doc_001_chunk_003",
    "vector": [0.12, -0.34, 0.81, 0.19],
    "metadata": {
        "document": "employee_policy.pdf",
        "page": 12,
        "department": "HR",
        "language": "en",
    },
}

print("Example vector database record:")
for key, value in record.items():
    print(f"{key}: {value}")

print("\nCollection:")
print("A logical group of vector records managed under a common schema/index configuration.")
