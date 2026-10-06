"""
09 - Query Processing
Prepare a user query before retrieval.
"""

query = "  How does RAG retrieve relevant documents?  "

clean_query = " ".join(query.strip().split())

print("Original:", repr(query))
print("Processed:", clean_query)

print("\nTypical production query processing can include:")
print("- normalization")
print("- query rewriting")
print("- intent detection")
print("- metadata/filter extraction")
