# 15 - Memory and Threads

threads = {
    "thread_001": [
        {"role": "human", "content": "My project uses RAG."},
        {"role": "ai", "content": "You can use retrieval and generation."}
    ],
    "thread_002": [
        {"role": "human", "content": "Explain LangGraph."}
    ]
}

for thread_id, messages in threads.items():
    print(f"\n{thread_id}")
    for message in messages:
        print(message["role"], ":", message["content"])
