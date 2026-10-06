"""
23 - Mini RAG Pipeline
End-to-end dependency-free demonstration using keyword matching.
"""

documents = [
    {"id": "d1", "text": "RAG retrieves external knowledge and gives it to an LLM as context."},
    {"id": "d2", "text": "Embeddings represent text as numerical vectors."},
    {"id": "d3", "text": "Chunking divides large documents into smaller retrieval units."}
]

query = "How does RAG use external knowledge?"

query_terms = set(query.lower().replace("?", "").split())

def score(text):
    terms = set(text.lower().replace(".", "").split())
    return len(query_terms & terms)

ranked = sorted(
    [(doc, score(doc["text"])) for doc in documents],
    key=lambda x: x[1],
    reverse=True
)

top_docs = [doc for doc, value in ranked[:2] if value > 0]

print("Query:", query)
print("\nRetrieved context:")
for doc in top_docs:
    print(f"[{doc['id']}] {doc['text']}")

print("\nPipeline:")
print("Query -> Retrieval -> Context -> Prompt -> LLM -> Grounded Answer")
