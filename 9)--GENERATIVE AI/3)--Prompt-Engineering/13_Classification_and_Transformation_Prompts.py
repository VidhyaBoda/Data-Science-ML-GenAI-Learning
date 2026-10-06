"""13 - Classification and transformation prompts"""

classification_prompt = """
Classify each support message as one of:
billing, technical, account, other.

Return only the category.
"""

transformation_prompt = """
Convert the supplied business requirement into:
1. User story
2. Acceptance criteria
3. Edge cases
"""

print("Classification prompt:")
print(classification_prompt)
print("\nTransformation prompt:")
print(transformation_prompt)
