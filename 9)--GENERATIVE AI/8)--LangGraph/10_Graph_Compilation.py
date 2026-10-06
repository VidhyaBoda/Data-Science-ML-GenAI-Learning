# 10 - Graph Compilation
# Conceptually, a builder is compiled into an executable graph.

class GraphBuilder:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, name, function):
        self.nodes[name] = function

    def add_edge(self, source, target):
        self.edges.append((source, target))

    def compile(self):
        return {
            "nodes": list(self.nodes.keys()),
            "edges": self.edges
        }

builder = GraphBuilder()
builder.add_node("process", lambda state: state)
builder.add_node("answer", lambda state: state)
builder.add_edge("process", "answer")

compiled_graph = builder.compile()
print(compiled_graph)
