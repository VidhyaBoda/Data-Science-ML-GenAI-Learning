"""03 - Instructions, context and constraints"""

instruction = "Explain customer churn."
context = "Audience: a business manager with limited technical knowledge."
constraints = [
    "Use simple language.",
    "Include 3 business implications.",
    "Do not invent numerical results.",
]

print("Instruction:", instruction)
print("Context:", context)
print("Constraints:")
for item in constraints:
    print("-", item)
