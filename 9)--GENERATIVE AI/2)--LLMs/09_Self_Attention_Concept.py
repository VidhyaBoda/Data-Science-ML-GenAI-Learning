"""09 - Self-attention concept"""

sentence = [
    "The", "analyst", "opened", "the", "report",
    "because", "it", "contained", "important", "results"
]

print("Example sentence:")
print(" ".join(sentence))

print("\nSelf-attention allows a token representation to incorporate")
print("information from other relevant tokens in the sequence.")

print("\nHigh-level idea:")
print("Queries + Keys + Values -> Attention scores -> Weighted information")
