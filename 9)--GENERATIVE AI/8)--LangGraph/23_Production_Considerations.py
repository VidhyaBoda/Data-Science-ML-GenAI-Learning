# 23 - Production Considerations

considerations = {
    "state_design": "Keep state explicit, minimal, and well-defined.",
    "routing": "Use deterministic routing where possible.",
    "persistence": "Choose checkpointing based on recovery requirements.",
    "security": "Validate tools, permissions, credentials, and external inputs.",
    "observability": "Trace nodes, transitions, latency, errors, and tool calls.",
    "evaluation": "Test complete workflows and individual nodes.",
    "cost": "Control loops, model calls, tool calls, and context size."
}

for key, value in considerations.items():
    print(f"{key}: {value}")
