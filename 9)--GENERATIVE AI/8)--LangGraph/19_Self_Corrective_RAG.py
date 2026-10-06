# 19 - Self-Corrective RAG

def grade_context(state):
    if state["relevance"] >= 0.8:
        return "generate"
    return "retry_retrieval"

examples = [
    {"relevance": 0.91},
    {"relevance": 0.52}
]

for state in examples:
    print(state, "->", grade_context(state))
