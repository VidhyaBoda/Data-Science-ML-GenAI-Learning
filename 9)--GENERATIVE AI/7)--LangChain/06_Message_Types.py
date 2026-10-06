# 06 - Message Types

messages = [
    ("system", "You are a professional AI tutor."),
    ("human", "What is a chain?"),
    ("ai", "A chain connects application steps."),
    ("human", "Why is that useful?")
]

for role, content in messages:
    print(f"{role.upper()}: {content}")
