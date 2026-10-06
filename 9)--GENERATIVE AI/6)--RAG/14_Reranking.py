"""
14 - Reranking
A second-stage model can rerank retrieved candidates.
"""

retrieved = [
    {"id": "d1", "retrieval_score": 0.82, "reranker_score": 0.61},
    {"id": "d2", "retrieval_score": 0.79, "reranker_score": 0.93},
    {"id": "d3", "retrieval_score": 0.76, "reranker_score": 0.72}
]

ranked = sorted(retrieved, key=lambda x: x["reranker_score"], reverse=True)

for item in ranked:
    print(item)
