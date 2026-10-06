# 16 - Tools and Tool Calling

def calculator(expression):
    return eval(expression, {"__builtins__": {}}, {})

tools = {"calculator": calculator}
expression = "25 * 4 + 10"
print("Tool:", "calculator")
print("Input:", expression)
print("Result:", tools["calculator"](expression))

print("Production note: validate tool inputs; never blindly execute arbitrary code.")
