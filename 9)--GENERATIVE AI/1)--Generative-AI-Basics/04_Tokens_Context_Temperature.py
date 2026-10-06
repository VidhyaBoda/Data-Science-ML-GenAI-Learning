"""
04 - Tokens, Context Window and Temperature

Learning objective:
Learn three important concepts used when working with LLMs.
"""

concepts = {
    "Token": (
        "A unit of text processed by a language model. "
        "A token can represent a word, part of a word, punctuation, or another text unit."
    ),
    "Context Window": (
        "The amount of input/output context a model can consider within a request."
    ),
    "Temperature": (
        "A generation control that influences randomness. Lower values generally "
        "produce more predictable output; higher values generally allow more variation."
    ),
}

for concept, explanation in concepts.items():
    print(f"{concept}:\n{explanation}\n")

print("Practical idea:")
print("- Low temperature -> useful when consistency matters.")
print("- Higher temperature -> useful when creative variation is desired.")
print("- Larger context window -> useful when an application needs more information in context.")
