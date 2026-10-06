# 24 - Mini LangGraph-Style Workflow
# Dependency-free simulation of a stateful graph.

def classify(state):
    state["category"] = "calculation" if any(ch.isdigit() for ch in state["query"]) else "general"
    return state

def route(state):
    return "calculate" if state["category"] == "calculation" else "respond"

def calculate(state):
    state["answer"] = "A calculation tool would be used here."
    return state

def respond(state):
    state["answer"] = "This is a general-information workflow."
    return state

state = {"query": "Calculate 25 * 4", "answer": None}

state = classify(state)
next_node = route(state)

if next_node == "calculate":
    state = calculate(state)
else:
    state = respond(state)

print("Final state:", state)
