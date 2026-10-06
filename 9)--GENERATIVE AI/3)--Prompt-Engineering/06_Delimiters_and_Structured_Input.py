"""06 - Delimiters and structured input"""

customer_feedback = """
The delivery was fast, but the packaging was damaged.
"""

prompt = f"""
Task: Extract the sentiment and main issue.

Customer feedback:
<feedback>
{customer_feedback.strip()}
</feedback>
"""

print(prompt)
print("\nDelimiters make boundaries between instructions and user-provided data clearer.")
print("Common choices: XML-like tags, triple quotes, JSON objects, or clearly labeled sections.")
