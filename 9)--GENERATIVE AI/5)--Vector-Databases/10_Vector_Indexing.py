"""10 - Vector indexing"""

indexing_goals = [
    "Reduce search latency",
    "Avoid scanning every vector",
    "Scale to large collections",
    "Balance recall, latency and memory",
]

for goal in indexing_goals:
    print("-", goal)

print("\nIndex configuration is an engineering trade-off.")
print("Higher retrieval recall can sometimes require more computation or memory.")
