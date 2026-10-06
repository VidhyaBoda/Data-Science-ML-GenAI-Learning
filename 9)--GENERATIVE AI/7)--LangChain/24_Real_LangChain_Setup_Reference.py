# 24 - Real LangChain Setup Reference
# Install the provider-specific package that matches your model provider.
# Example: pip install -U langchain langchain-openai
#
# Keep API keys in environment variables, never hard-code secrets.

example_code = '''
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI(model="YOUR_MODEL_NAME")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

chain = prompt | model

response = chain.invoke({
    "question": "What is LangChain?"
})

print(response.content)
'''

print(example_code)
