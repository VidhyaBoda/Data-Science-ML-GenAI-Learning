"""05 - Zero-shot, one-shot and few-shot prompting"""

patterns = {
    "Zero-shot": "Instruction without examples.",
    "One-shot": "Instruction with one input-output example.",
    "Few-shot": "Instruction with multiple examples showing the desired pattern.",
}

for name, meaning in patterns.items():
    print(f"{name}: {meaning}")

print("\nUse examples when the desired format, classification boundary, or style is difficult to describe precisely.")
