# 19 - Memory and Conversation State

conversation = []

def add_message(role, content):
    conversation.append({"role": role, "content": content})

add_message("human", "My project is about RAG.")
add_message("ai", "Great. RAG combines retrieval and generation.")
add_message("human", "What should I learn next?")

for message in conversation:
    print(f"{message['role']}: {message['content']}")

print("State is application data; production systems should define retention and privacy rules.")
