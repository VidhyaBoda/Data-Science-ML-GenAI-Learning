"""11 - Inference and text generation"""

def inference_pipeline(prompt):
    steps = [
        f"1. Receive prompt: {prompt}",
        "2. Tokenize the prompt",
        "3. Run tokens through the trained model",
        "4. Produce a probability distribution for the next token",
        "5. Select/sample a token using a decoding strategy",
        "6. Append the token to the sequence",
        "7. Repeat until a stopping condition is reached",
        "8. Decode tokens into readable text",
    ]
    print("\n".join(steps))

inference_pipeline("Explain data cleaning.")
