"""
02 - AI, Machine Learning, Deep Learning and Generative AI

Learning objective:
Understand the hierarchy and relationship among these concepts.
"""

concepts = {
    "Artificial Intelligence (AI)": "Broad field of building systems that perform tasks requiring intelligence.",
    "Machine Learning (ML)": "A subset of AI where systems learn patterns from data.",
    "Deep Learning (DL)": "A subset of ML based mainly on multi-layer neural networks.",
    "Generative AI": "AI systems designed to generate new content based on learned patterns.",
}

for name, description in concepts.items():
    print(f"{name}\n  {description}\n")

print("Simple mental model:")
print("AI")
print("└── Machine Learning")
print("    └── Deep Learning")
print("        └── Some modern Generative AI systems")
print()
print("Important: Generative AI is not simply another name for Deep Learning.")
print("Modern GenAI commonly uses deep neural networks, but the concepts are not identical.")
