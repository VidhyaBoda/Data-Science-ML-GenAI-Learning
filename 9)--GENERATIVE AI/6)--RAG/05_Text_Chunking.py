"""
05 - Text Chunking
Chunk documents into smaller retrieval units.
"""

text = """
RAG systems often split large documents into smaller chunks.
Chunking improves retrieval granularity because the retriever can
return only the sections relevant to a user's question.
"""

def chunk_text(text, chunk_size=90):
    text = " ".join(text.split())
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

chunks = chunk_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}: {chunk}")
