# 09 - START and END

graph = {
    "START": "process_input",
    "process_input": "generate_answer",
    "generate_answer": "END"
}

for current, next_node in graph.items():
    print(f"{current} -> {next_node}")
