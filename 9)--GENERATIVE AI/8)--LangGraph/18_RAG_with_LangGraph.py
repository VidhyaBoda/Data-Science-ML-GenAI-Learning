# 18 - RAG with LangGraph

rag_graph = {
    "START": "retrieve",
    "retrieve": "grade_context",
    "grade_context": "generate",
    "generate": "END"
}

for source, target in rag_graph.items():
    print(f"{source} -> {target}")

print("\nPossible conditional extension:")
print("grade_context -> retry_retrieval when evidence is insufficient")
