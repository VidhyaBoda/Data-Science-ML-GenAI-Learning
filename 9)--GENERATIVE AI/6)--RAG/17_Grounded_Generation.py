"""
17 - Grounded Generation
Illustrates the principle of answering from retrieved evidence.
"""

context = [
    "The HR portal supports annual leave applications.",
    "Employees should submit requests before the planned leave date."
]

question = "Where can employees apply for annual leave?"

print("Question:", question)
print("\nEvidence:")
for item in context:
    print("-", item)

print("\nGrounded answer:")
print("Employees can apply for annual leave through the HR portal.")
