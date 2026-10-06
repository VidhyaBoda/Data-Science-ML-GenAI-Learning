"""08 - Reasoning requests and task decomposition"""

task = "Analyze a customer churn problem."

steps = [
    "Define the business question.",
    "Identify required data.",
    "Check data quality.",
    "Choose relevant metrics.",
    "Analyze patterns.",
    "Generate actionable recommendations.",
    "Validate conclusions.",
]

print("Task:", task)
print("\nDecomposed workflow:")
for i, step in enumerate(steps, 1):
    print(f"{i}. {step}")

print("\nProfessional practice:")
print("Ask for concise conclusions, assumptions and validation evidence rather than relying on unverifiable hidden reasoning.")
