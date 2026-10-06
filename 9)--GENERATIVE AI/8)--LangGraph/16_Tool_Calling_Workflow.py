# 16 - Tool Calling Workflow

def choose_tool(state):
    return "calculator" if state["requires_calculation"] else "answer"

def calculator(state):
    state["tool_result"] = 125 * 4
    return state

def answer(state):
    state["answer"] = f"Calculated result: {state.get('tool_result', 'N/A')}"
    return state

state = {"requires_calculation": True}

next_node = choose_tool(state)
print("Selected:", next_node)

if next_node == "calculator":
    state = calculator(state)
    state = answer(state)

print(state)
