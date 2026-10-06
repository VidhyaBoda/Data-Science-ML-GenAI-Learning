# 07 - Edges and Routing

def route(state):
    if state["needs_tool"]:
        return "tool"
    return "answer"

states = [
    {"needs_tool": True},
    {"needs_tool": False}
]

for state in states:
    print("State:", state, "-> next node:", route(state))
