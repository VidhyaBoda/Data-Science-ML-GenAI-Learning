# 08 - Runnables and LCEL
# LCEL connects runnable components into a composable pipeline.

def prompt(user_input):
    return f"Explain this topic briefly: {user_input}"

def model(prompt_text):
    return f"[MODEL] {prompt_text}"

def parser(model_output):
    return model_output.replace("[MODEL] ", "")

result = parser(model(prompt("LangChain Runnable")))
print(result)
print("Conceptual LCEL flow: prompt | model | parser")
