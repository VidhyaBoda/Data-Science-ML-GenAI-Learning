# 04 - Chat Models

class ChatModel:
    def invoke(self, messages):
        return f"Model response for: {messages[-1]['content']}"

model = ChatModel()
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain LangChain."}
]

print(model.invoke(messages))
