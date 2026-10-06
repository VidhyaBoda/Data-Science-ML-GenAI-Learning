"""16 - Prompting for Retrieval-Augmented Generation"""

rag_prompt = """
Answer the user's question using ONLY the supplied retrieved context.

Rules:
1. If the context does not contain the answer, say that the answer is not available in the provided context.
2. Do not invent citations or facts.
3. Distinguish direct evidence from reasonable interpretation.
4. Cite the supplied context identifiers when available.

Retrieved context:
<context>
{retrieved_chunks}
</context>

Question:
{question}
"""

print(rag_prompt)
print("\nRAG prompting is covered here conceptually; implementation comes after embeddings and vector databases.")
