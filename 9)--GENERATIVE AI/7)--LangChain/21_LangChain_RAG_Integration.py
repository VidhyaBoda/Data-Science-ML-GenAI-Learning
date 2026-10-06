# 21 - LangChain + RAG Integration

pipeline = [
    "Load documents",
    "Split documents into chunks",
    "Create embeddings",
    "Store vectors",
    "Receive user query",
    "Retrieve relevant chunks",
    "Build prompt with context",
    "Call chat model",
    "Parse response",
    "Return answer with sources"
]

for step in pipeline:
    print("->", step)
