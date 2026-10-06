# 13 - Human-in-the-Loop

workflow = {
    "draft": "Generated response requiring approval.",
    "approval": None,
    "status": "waiting_for_human"
}

print("Workflow paused for human review.")
workflow["approval"] = "approved"
workflow["status"] = "continue"

print(workflow)
