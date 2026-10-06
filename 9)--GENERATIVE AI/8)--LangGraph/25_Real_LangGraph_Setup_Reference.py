# 25 - Real LangGraph Setup Reference
# Example package installation:
# pip install -U langgraph langchain
#
# The following is a reference pattern. Provider/model packages depend on
# the model service you choose.

example_code = '''
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message: str

def process(state: State):
    return {"message": state["message"].upper()}

builder = StateGraph(State)

builder.add_node("process", process)
builder.add_edge(START, "process")
builder.add_edge("process", END)

graph = builder.compile()

result = graph.invoke({"message": "hello langgraph"})
print(result)
'''

print(example_code)
