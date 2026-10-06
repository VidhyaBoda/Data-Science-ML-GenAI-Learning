"""
06 - Chunking Strategies
Compare conceptual chunking strategies.
"""

strategies = {
    "fixed_size": "Split text after a fixed character/token length.",
    "sentence_based": "Keep complete sentences together.",
    "paragraph_based": "Use paragraphs as retrieval units.",
    "recursive": "Split using a hierarchy of separators.",
    "semantic": "Create chunks around semantic coherence."
}

for name, description in strategies.items():
    print(f"{name}: {description}")
