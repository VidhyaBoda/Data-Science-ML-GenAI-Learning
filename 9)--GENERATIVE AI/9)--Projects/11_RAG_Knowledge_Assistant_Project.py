# Portfolio-ready RAG project blueprint.
pipeline = [
    "Collect trusted documents",
    "Extract and clean text",
    "Chunk documents",
    "Generate embeddings",
    "Store vectors + metadata",
    "Retrieve relevant chunks",
    "Build grounded prompt",
    "Generate answer",
    "Return citations",
    "Evaluate retrieval and answer quality",
]
print(" -> ".join(pipeline))
