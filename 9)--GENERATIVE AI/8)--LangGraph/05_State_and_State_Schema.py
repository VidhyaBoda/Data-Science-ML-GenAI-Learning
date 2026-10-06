# 05 - State and State Schema

state = {
    "user_query": "Find information about RAG.",
    "context": [],
    "answer": None,
    "steps": []
}

print("Initial state:")
for key, value in state.items():
    print(f"{key}: {value}")

print("\nA state schema defines the fields and types that nodes can read or update.")
