"""05 - Insert and index vectors"""

records = [
    {"id": "doc1", "vector": [0.1, 0.2, 0.3]},
    {"id": "doc2", "vector": [0.2, 0.1, 0.4]},
]

print("Insert records:")
for record in records:
    print("-", record)

print("\nConceptual indexing workflow:")
print("Create collection -> define vector dimension/metric -> insert records -> build/maintain index")
