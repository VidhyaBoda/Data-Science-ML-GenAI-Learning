"""20 - Professional reusable prompt patterns"""

patterns = {
    "Analysis": [
        "Objective",
        "Context/data",
        "Analysis dimensions",
        "Constraints",
        "Expected output",
        "Validation requirements",
    ],
    "Extraction": [
        "Source text",
        "Fields to extract",
        "Allowed values/types",
        "Missing-value behavior",
        "Output schema",
    ],
    "RAG QA": [
        "Retrieved context",
        "Question",
        "Grounding rule",
        "Citation rule",
        "Unknown-answer behavior",
    ],
}

for pattern, sections in patterns.items():
    print(f"\n{pattern}")
    for section in sections:
        print(f"  - {section}")

print("\nBest practice:")
print("Build prompts as reusable, testable components instead of one-off paragraphs.")
