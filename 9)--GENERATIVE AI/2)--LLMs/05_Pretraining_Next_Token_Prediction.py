"""05 - Pretraining and next-token prediction"""

sequence = ["Generative", "AI", "uses", "models", "to"]

print("Example token sequence:")
print(" ".join(sequence))

print("\nConceptual objective:")
print("The model uses the previous context to estimate the probability of the next token.")

print("\nTraining loop concept:")
print("Text -> Tokens -> Context -> Next-token prediction -> Loss -> Backpropagation -> Parameter update")
