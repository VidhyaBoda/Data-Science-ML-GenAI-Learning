# 09 - Chains Basics

def retrieve(topic):
    return f"Context about {topic}"

def generate(context, question):
    return f"Context: {context}\nQuestion: {question}"

question = "What is a LangChain chain?"
print(generate(retrieve("LangChain chains"), question))
