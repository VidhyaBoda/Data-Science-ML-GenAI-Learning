# 18 - Agent Workflow

steps = [
    "Receive user request",
    "Understand task",
    "Select tool or action",
    "Execute tool",
    "Observe result",
    "Decide whether more steps are required",
    "Return final answer"
]

for i, step in enumerate(steps, 1):
    print(f"{i}. {step}")
