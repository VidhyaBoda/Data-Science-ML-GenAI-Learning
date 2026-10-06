"""04 - Encoder, decoder and decoder-only architectures"""

architectures = {
    "Encoder-only": "Best known for understanding/representation tasks.",
    "Encoder-decoder": "Uses an encoder to process input and a decoder to generate output.",
    "Decoder-only": "Generates output autoregressively and is widely used for modern LLMs.",
}

for name, description in architectures.items():
    print(f"{name}: {description}")

print("\nKey distinction:")
print("Architecture choice depends on the task and training objective.")
