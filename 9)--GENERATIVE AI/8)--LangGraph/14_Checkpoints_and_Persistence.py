# 14 - Checkpoints and Persistence

checkpoint = {
    "thread_id": "demo-thread-001",
    "step": "tool_execution",
    "state": {
        "query": "Calculate revenue growth",
        "result": None
    }
}

print("Checkpoint:")
print(checkpoint)

print("\nPurpose:")
print("- Resume interrupted workflows")
print("- Preserve state between steps")
print("- Support human review")
print("- Improve debugging and observability")
