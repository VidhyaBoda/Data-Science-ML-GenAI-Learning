# 11 - Simple Stateful Graph

def receive(state):
    state["steps"].append("receive")
    return state

def process(state):
    state["result"] = state["input"].upper()
    state["steps"].append("process")
    return state

def finish(state):
    state["steps"].append("finish")
    return state

state = {"input": "langgraph", "result": None, "steps": []}

for node in [receive, process, finish]:
    state = node(state)

print(state)
