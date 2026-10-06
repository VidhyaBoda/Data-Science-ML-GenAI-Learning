"""08 - Metadata filtering"""

records = [
    {"id": "d1", "score": 0.91, "department": "HR"},
    {"id": "d2", "score": 0.89, "department": "Finance"},
    {"id": "d3", "score": 0.87, "department": "HR"},
    {"id": "d4", "score": 0.82, "department": "IT"},
]

target_department = "HR"

filtered = [
    record for record in records
    if record["department"] == target_department
]

print(f"Records filtered for department={target_department}:")
for record in filtered:
    print(record)

print("\nProduction vector search often combines similarity with metadata filters.")
