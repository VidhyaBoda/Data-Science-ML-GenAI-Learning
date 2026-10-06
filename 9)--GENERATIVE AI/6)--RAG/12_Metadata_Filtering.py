"""
12 - Metadata Filtering
Combine semantic retrieval with metadata constraints.
"""

records = [
    {"id": "d1", "text": "Leave policy", "department": "HR", "year": 2026},
    {"id": "d2", "text": "Travel policy", "department": "Finance", "year": 2026},
    {"id": "d3", "text": "Old leave policy", "department": "HR", "year": 2024}
]

filtered = [
    r for r in records
    if r["department"] == "HR" and r["year"] >= 2026
]

print("Filtered records:")
for record in filtered:
    print(record)
