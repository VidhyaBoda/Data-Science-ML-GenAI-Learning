"""
01 - What Is RAG?
Retrieval-Augmented Generation combines retrieval with generation.
"""

documents = [
    "RAG retrieves relevant external knowledge before generating an answer.",
    "An LLM can generate fluent text but may not know private or recent data.",
    "A RAG system typically contains ingestion, retrieval, prompt construction, and generation."
]

query = "Why is RAG useful?"

print("Query:", query)
print("\nAvailable knowledge:")
for doc in documents:
    print("-", doc)

print("\nKey idea:")
print("Retrieve relevant context -> provide it to the LLM -> generate a grounded answer.")
