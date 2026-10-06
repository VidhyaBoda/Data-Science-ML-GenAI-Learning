# 01 - What Is LangGraph
# LangGraph is designed for building stateful, graph-based LLM workflows and agents.

concept = {
    "core_idea": "Represent an application as states and connected nodes.",
    "state": "Shared data carried through the workflow.",
    "node": "A unit of work that reads and/or updates state.",
    "edge": "A connection that determines what runs next.",
    "strength": "Useful for controllable, stateful, multi-step agent workflows."
}

for key, value in concept.items():
    print(f"{key}: {value}")
