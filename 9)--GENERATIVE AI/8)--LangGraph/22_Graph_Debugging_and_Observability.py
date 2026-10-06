# 22 - Graph Debugging and Observability

events = []

def log_event(node, state):
    events.append({
        "node": node,
        "step": len(events) + 1,
        "state_keys": list(state.keys())
    })

state = {"query": "Explain agents", "answer": None}

for node in ["retrieve", "generate", "finalize"]:
    log_event(node, state)

for event in events:
    print(event)
