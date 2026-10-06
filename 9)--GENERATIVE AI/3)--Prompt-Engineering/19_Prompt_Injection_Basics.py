"""19 - Prompt injection basics"""

print("Prompt injection occurs when untrusted content attempts to influence")
print("the behavior of an AI application in unintended ways.")

print("\nExample risk:")
print("A retrieved document contains instructions such as 'ignore previous rules'.")
print("The application should treat retrieved content as data, not automatically as trusted instructions.")

print("\nDefensive principles:")
principles = [
    "Separate trusted instructions from untrusted data.",
    "Use clear delimiters and explicit instruction hierarchy.",
    "Limit tool permissions.",
    "Validate tool arguments and outputs.",
    "Do not expose secrets to the model unnecessarily.",
    "Test adversarial inputs before production deployment.",
]

for principle in principles:
    print("-", principle)
