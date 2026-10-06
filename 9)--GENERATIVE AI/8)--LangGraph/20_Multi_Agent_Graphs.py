# 20 - Multi-Agent Graphs

agents = {
    "researcher": "Find and summarize relevant information.",
    "analyst": "Analyze the retrieved information.",
    "writer": "Produce the final response."
}

edges = [
    ("researcher", "analyst"),
    ("analyst", "writer")
]

print("Agents:")
for name, role in agents.items():
    print(f"- {name}: {role}")

print("\nFlow:")
for source, target in edges:
    print(f"{source} -> {target}")
