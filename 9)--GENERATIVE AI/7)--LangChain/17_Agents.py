# 17 - Agents

tools = {
    "calculator": "Performs numerical calculations",
    "search": "Retrieves information from a knowledge source"
}

question = "I need a numerical calculation."
selected_tool = "calculator" if "calculation" in question.lower() else "search"

print("Question:", question)
print("Selected tool:", selected_tool)
print("Purpose:", tools[selected_tool])
