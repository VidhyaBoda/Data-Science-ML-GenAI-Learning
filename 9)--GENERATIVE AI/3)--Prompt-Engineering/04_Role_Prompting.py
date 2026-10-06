"""04 - Role prompting"""

roles = {
    "Data Analyst": "Focus on metrics, trends, anomalies and business implications.",
    "Python Developer": "Focus on readable, tested and maintainable Python.",
    "ML Engineer": "Focus on model design, evaluation and production considerations.",
}

for role, behavior in roles.items():
    print(f"\nRole: {role}")
    print("Expected behavior:", behavior)

print("\nImportant:")
print("A role should guide the task; it does not grant real-world authority or access.")
