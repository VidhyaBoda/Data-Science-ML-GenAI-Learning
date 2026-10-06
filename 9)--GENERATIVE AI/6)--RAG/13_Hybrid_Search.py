"""
13 - Hybrid Search
Combine semantic/vector retrieval with keyword retrieval.
"""

keyword_scores = {"d1": 0.90, "d2": 0.30, "d3": 0.70}
semantic_scores = {"d1": 0.75, "d2": 0.80, "d3": 0.60}

alpha = 0.6
combined = {}

for doc_id in keyword_scores:
    combined[doc_id] = (
        alpha * semantic_scores[doc_id]
        + (1 - alpha) * keyword_scores[doc_id]
    )

print("Combined ranking:")
for doc_id, score in sorted(combined.items(), key=lambda x: x[1], reverse=True):
    print(doc_id, round(score, 4))
