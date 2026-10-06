"""13 - CRUD operations for vector records"""

operations = {
    "Create": "Insert a new vector record.",
    "Read": "Retrieve a record or search for similar vectors.",
    "Update": "Replace/update vector or metadata.",
    "Delete": "Remove a vector record.",
}

for operation, description in operations.items():
    print(f"{operation}: {description}")

print("\nReal vector databases provide persistence, indexing and APIs around these operations.")
