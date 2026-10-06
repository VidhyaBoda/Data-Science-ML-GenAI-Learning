"""15 - LLM limitations"""

limitations = [
    "Hallucination: fluent output can contain unsupported or incorrect claims.",
    "Knowledge may be incomplete or outdated.",
    "Outputs can be sensitive to prompt wording.",
    "Models can reproduce undesirable patterns from training data.",
    "Long-context processing can still be imperfect.",
    "Generated code and SQL require testing and validation.",
]

print("LLM limitations:")
for item in limitations:
    print(f"- {item}")

print("\nProfessional rule:")
print("Treat LLM output as generated content that requires appropriate validation,")
print("especially in high-impact or production workflows.")
