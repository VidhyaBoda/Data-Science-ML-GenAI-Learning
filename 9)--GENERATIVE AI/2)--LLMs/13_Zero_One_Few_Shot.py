"""13 - Zero-shot, one-shot and few-shot prompting"""

examples = {
    "Zero-shot": "Task instruction without an example.",
    "One-shot": "Task instruction with one example.",
    "Few-shot": "Task instruction with multiple examples.",
}

for name, explanation in examples.items():
    print(f"{name}: {explanation}")

print("\nWhy examples help:")
print("They demonstrate the expected input/output pattern and can reduce ambiguity.")
