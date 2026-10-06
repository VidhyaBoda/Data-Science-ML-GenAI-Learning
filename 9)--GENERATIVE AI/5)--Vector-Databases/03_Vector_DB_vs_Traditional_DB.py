"""03 - Vector database vs traditional database"""

comparison = {
    "Traditional relational DB": [
        "Strong structured schema",
        "SQL-based filtering and joins",
        "Excellent transactional workloads",
        "Exact-value/range queries",
    ],
    "Vector database": [
        "Vector storage and similarity search",
        "Nearest-neighbor retrieval",
        "Metadata filtering around vector search",
        "Commonly used for semantic retrieval",
    ],
}

for database, characteristics in comparison.items():
    print(f"\n{database}")
    for item in characteristics:
        print("-", item)

print("\nModern applications can use both systems together.")
