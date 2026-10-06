"""
16 - RAG Prompt Template
Ground the answer in retrieved context.
"""

question = "How should an employee apply for leave?"
context = """
Employees can apply for annual leave through the HR portal.
Leave requests should be submitted before the planned leave date.
"""

prompt = f"""Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Rules:
- Do not invent facts.
- If the context is insufficient, say so.
- Keep the answer concise.
"""

print(prompt)
