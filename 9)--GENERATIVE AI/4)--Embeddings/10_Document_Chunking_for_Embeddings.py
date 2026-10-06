"""10 - Document chunking for embeddings"""

document = """
Generative AI applications often work with documents that are too large
to place into a single model context. Chunking divides the document into
smaller sections that can be embedded and retrieved independently.
""".strip()

chunk_size = 20
words = document.split()
chunks = [
    " ".join(words[i:i + chunk_size])
    for i in range(0, len(words), chunk_size)
]

print("Document chunks:")
for i, chunk in enumerate(chunks, 1):
    print(f"\nChunk {i}: {chunk}")

print("\nProduction chunking should consider semantic boundaries, overlap,")
print("document structure, model context limits and retrieval quality.")
