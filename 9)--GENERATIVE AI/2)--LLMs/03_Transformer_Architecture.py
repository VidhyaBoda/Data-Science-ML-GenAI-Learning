"""03 - Transformer architecture overview"""

def transformer_flow():
    steps = [
        "Input text",
        "Tokenization",
        "Token embeddings + positional information",
        "Transformer blocks",
        "Attention mechanisms",
        "Feed-forward networks",
        "Output representation / next-token probabilities",
    ]

    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

print("Transformer architecture is the foundation of most modern LLMs.")
transformer_flow()
