"""
03 - RAG Architecture
Learning the end-to-end RAG flow.
"""

flow = [
    "1. Documents / knowledge sources",
    "2. Document loading",
    "3. Text cleaning and chunking",
    "4. Embedding generation",
    "5. Vector database/index",
    "6. User query",
    "7. Query embedding",
    "8. Similarity retrieval",
    "9. Context construction",
    "10. LLM generation",
    "11. Grounded answer"
]

print("RAG Architecture")
print("=" * 40)
for step in flow:
    print(step)
