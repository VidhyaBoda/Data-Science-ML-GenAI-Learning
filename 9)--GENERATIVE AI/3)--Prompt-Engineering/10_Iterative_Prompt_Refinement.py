"""10 - Iterative prompt refinement"""

versions = [
    "Explain sales.",
    "Explain the sales trend for a business manager.",
    "Explain the sales trend for a business manager using the provided monthly data. "
    "Identify the top 3 changes, cite the supplied values, and separate facts from hypotheses."
]

for i, prompt in enumerate(versions, 1):
    print(f"Version {i}:\n{prompt}\n")

print("Refinement principle: increase specificity where the model has room to interpret the task incorrectly.")
