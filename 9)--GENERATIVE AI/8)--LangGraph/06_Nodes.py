# 06 - Nodes
# A node is a function that performs one step in the graph.

def retrieve_node(state):
    state["context"] = ["RAG retrieves external knowledge."]
    state["steps"].append("retrieve")
    return state

def answer_node(state):
    state["answer"] = "RAG combines retrieval with generation."
    state["steps"].append("answer")
    return state

state = {"context": [], "answer": None, "steps": []}

state = retrieve_node(state)
state = answer_node(state)

print(state)
