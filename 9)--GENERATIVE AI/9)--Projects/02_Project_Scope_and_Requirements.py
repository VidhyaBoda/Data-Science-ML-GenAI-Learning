# Define MVP scope before implementation.
mvp = {
    "must_have": [
        "Data ingestion",
        "EDA",
        "KPI dashboard",
        "GenAI insight generation",
        "Project README"
    ],
    "nice_to_have": [
        "RAG assistant",
        "Automated reports",
        "Role-based dashboard"
    ],
    "out_of_scope": ["Autonomous production decisions"]
}
print("MVP scope:")
for group, items in mvp.items():
    print(f"\n{group.upper()}")
    for item in items:
        print("-", item)
