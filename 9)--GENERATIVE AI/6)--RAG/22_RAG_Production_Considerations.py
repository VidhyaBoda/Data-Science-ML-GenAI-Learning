"""
22 - RAG Production Considerations
"""

considerations = {
    "quality": "Evaluate retrieval and grounded generation separately.",
    "security": "Control access to documents and prevent prompt injection through retrieved content.",
    "freshness": "Design ingestion and re-indexing strategies.",
    "latency": "Optimize embedding, retrieval, reranking, and generation.",
    "cost": "Control chunk count, retrieved context, model usage, and caching.",
    "observability": "Log queries, retrieved documents, scores, latency, and failures."
}

for key, value in considerations.items():
    print(f"{key}: {value}")
