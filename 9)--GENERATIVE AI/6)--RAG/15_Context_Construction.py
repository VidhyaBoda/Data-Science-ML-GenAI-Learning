"""
15 - Context Construction
Build the context that will be passed to the generator.
"""

retrieved_chunks = [
    {"source": "policy.md", "text": "Employees can apply for annual leave through the HR portal."},
    {"source": "policy.md", "text": "Leave requests should be submitted before the planned leave date."}
]

context_parts = []
for chunk in retrieved_chunks:
    context_parts.append(f"[Source: {chunk['source']}]\n{chunk['text']}")

context = "\n\n".join(context_parts)

print(context)
