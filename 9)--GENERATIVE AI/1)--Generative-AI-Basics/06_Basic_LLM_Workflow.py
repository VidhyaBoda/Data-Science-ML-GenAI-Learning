"""
06 - Basic LLM Workflow

This is a conceptual implementation. It intentionally does not require
an API key or external package.

Learning objective:
Understand the basic flow of an LLM-powered application.
"""

def basic_llm_workflow(user_prompt: str):
    if not user_prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    workflow = [
        "1. User provides a prompt",
        "2. Application validates/prepares the input",
        "3. Prompt is converted into tokens",
        "4. Model processes the input in context",
        "5. Model generates output tokens",
        "6. Application converts the output into user-readable text",
    ]

    print("LLM APPLICATION WORKFLOW\n")
    for step in workflow:
        print(step)

    print(f"\nExample user prompt: {user_prompt}")
    print("Example model output: [Generated response would appear here]")


if __name__ == "__main__":
    basic_llm_workflow("Explain Generative AI in simple terms.")
