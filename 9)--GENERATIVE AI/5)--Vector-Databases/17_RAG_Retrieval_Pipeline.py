"""17 - RAG retrieval pipeline"""

pipeline = [
    "User question",
    "Query embedding",
    "Vector search",
    "Metadata filtering",
    "Optional reranking",
    "Relevant chunks",
    "Prompt construction",
    "LLM generation",
    "Grounded answer",
]

print(" -> ".join(pipeline))
print("\nThe vector database is primarily responsible for the retrieval layer.")
