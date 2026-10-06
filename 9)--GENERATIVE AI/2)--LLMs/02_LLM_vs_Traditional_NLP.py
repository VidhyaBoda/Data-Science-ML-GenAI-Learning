"""02 - LLMs vs Traditional NLP"""

comparison = {
    "Traditional NLP": [
        "Often task-specific",
        "May require manually designed features or task-specific training",
        "Usually optimized for a defined objective",
    ],
    "Modern LLM": [
        "Pretrained on broad text corpora",
        "Can perform many tasks through instructions/prompts",
        "Can be adapted with prompting, fine-tuning or retrieval",
    ],
}

for approach, points in comparison.items():
    print(f"\n{approach}")
    for point in points:
        print(f"- {point}")

print("\nImportant:")
print("LLMs are not automatically factual databases. Their generated output must be validated.")
