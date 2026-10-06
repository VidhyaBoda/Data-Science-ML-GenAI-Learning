# 08 - Conditional Edges

def decide_next(state):
    if state["confidence"] >= 0.8:
        return "final_answer"
    if state["retry_count"] < 2:
        return "retry"
    return "fallback"

examples = [
    {"confidence": 0.92, "retry_count": 0},
    {"confidence": 0.55, "retry_count": 0},
    {"confidence": 0.40, "retry_count": 2}
]

for state in examples:
    print(state, "->", decide_next(state))
