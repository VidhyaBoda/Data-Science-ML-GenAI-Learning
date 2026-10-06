"""
01 - What is Generative AI?

Learning objective:
Understand what Generative AI is, what it generates, and how it differs
from systems that only classify or predict.
"""

def explain_generative_ai():
    definition = (
        "Generative AI is a class of AI systems that learns patterns from "
        "data and generates new content such as text, images, audio, video, "
        "or code."
    )

    examples = {
        "Text": "Generate an email, summary, explanation, or article",
        "Code": "Generate or explain Python, SQL, Java, etc.",
        "Image": "Generate an image from a text description",
        "Audio": "Generate speech or music",
        "Video": "Generate or transform video content",
    }

    print("WHAT IS GENERATIVE AI?\n")
    print(definition)
    print("\nExamples:")
    for content_type, example in examples.items():
        print(f"- {content_type}: {example}")


if __name__ == "__main__":
    explain_generative_ai()
