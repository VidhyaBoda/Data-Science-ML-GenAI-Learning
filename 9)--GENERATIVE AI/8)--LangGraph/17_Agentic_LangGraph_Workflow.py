# 17 - Agentic LangGraph Workflow

workflow = [
    "Receive task",
    "Reason about next action",
    "Select tool",
    "Execute tool",
    "Observe result",
    "Evaluate result",
    "Retry or continue",
    "Return final response"
]

for i, step in enumerate(workflow, 1):
    print(f"{i}. {step}")
