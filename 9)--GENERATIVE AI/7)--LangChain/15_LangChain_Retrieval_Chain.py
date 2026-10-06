# 15 - Retrieval Chain

def retrieve(query):
    return {
        "langchain": "LangChain helps compose LLM application workflows.",
        "retrieval": "Retrieval finds relevant external context."
    }

def build_context(results):
    return "\n".join(results.values())

def generate(question, context):
    return f"Question: {question}\nContext: {context}\n\nGrounded response."

question = "What does LangChain help developers build?"
context = build_context(retrieve(question))
print(generate(question, context))
