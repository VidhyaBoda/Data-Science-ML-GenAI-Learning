# Example agentic workflow.
workflow = {
    "planner": "Break the user request into tasks",
    "retriever": "Fetch relevant knowledge",
    "analyst": "Compute or inspect required metrics",
    "writer": "Prepare the response",
    "reviewer": "Check factuality, format, and completeness",
}
for role, responsibility in workflow.items():
    print(f"{role.title():10} | {responsibility}")
