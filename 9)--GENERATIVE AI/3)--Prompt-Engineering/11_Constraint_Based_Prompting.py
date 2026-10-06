"""11 - Constraint-based prompting"""

constraints = [
    "Maximum 120 words",
    "Use a professional tone",
    "Use exactly 5 bullet points",
    "Use only information present in the supplied context",
    "If information is missing, state 'Insufficient information'",
]

print("Example constraint set:")
for constraint in constraints:
    print("-", constraint)

print("\nConstraints should be testable whenever possible.")
