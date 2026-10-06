"""
02 - RAG vs Traditional LLM
Conceptual comparison.
"""

traditional_llm = {
    "knowledge_source": "Model parameters",
    "external_private_data": "Not directly available",
    "fresh_information": "Limited unless connected to tools/data",
    "grounding": "Depends on prompt/model knowledge"
}

rag = {
    "knowledge_source": "Retrieved external documents + model parameters",
    "external_private_data": "Supported through retrieval",
    "fresh_information": "Can retrieve updated documents",
    "grounding": "Uses retrieved context"
}

print("Traditional LLM:")
for k, v in traditional_llm.items():
    print(f"{k}: {v}")

print("\nRAG:")
for k, v in rag.items():
    print(f"{k}: {v}")
