"""
20 - Common RAG Failures
"""

failures = {
    "poor_chunking": "Relevant information is split across unsuitable chunks.",
    "bad_retrieval": "The correct evidence is not retrieved.",
    "too_much_context": "Irrelevant context distracts the generator.",
    "missing_context": "The answer requires information not retrieved.",
    "stale_index": "The vector store contains outdated content.",
    "hallucination": "The model adds unsupported information.",
    "weak_evaluation": "A system is deployed without measuring retrieval and generation quality."
}

for failure, explanation in failures.items():
    print(f"{failure}: {explanation}")
