"""08 - Context window"""

print("Context window = the amount of tokenized context a model can process")
print("for a request, subject to the model's configured limits.")

print("\nWhy it matters:")
print("- Determines how much conversation/document context can be supplied.")
print("- Large documents may need chunking or retrieval.")
print("- Context limits are model-specific and can change over time.")

print("\nPractical architecture:")
print("Large documents -> Chunking -> Retrieval -> Relevant context -> LLM")
