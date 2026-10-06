# 21 - Error Handling and Retry

def execute(state):
    state["attempts"] += 1
    if state["attempts"] < 2:
        raise RuntimeError("Temporary tool failure")
    state["result"] = "Success"
    return state

state = {"attempts": 0, "result": None}

while state["attempts"] < 3:
    try:
        state = execute(state)
        break
    except RuntimeError as error:
        print("Error:", error)
        print("Retrying...")

print("Final:", state)
