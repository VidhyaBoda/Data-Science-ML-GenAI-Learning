# 13 - Text Splitters

text = "LangChain applications process documents. Large documents can be split into smaller chunks. Smaller chunks can improve retrieval precision."
words = text.split()
chunk_size = 8

chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}")
