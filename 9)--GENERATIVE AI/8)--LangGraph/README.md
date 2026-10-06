# 08--LangGraph

## LangGraph — Stateful Graph-Based LLM Workflows

This folder teaches **LangGraph** from fundamentals to stateful workflows, conditional routing, loops, persistence, human-in-the-loop, tool calling, agentic workflows, RAG, multi-agent systems, debugging, and production practices.

## Learning Flow

1. What is LangGraph
2. Core concepts
3. LangGraph vs LangChain
4. Graph architecture
5. State and state schema
6. Nodes
7. Edges and routing
8. Conditional edges
9. START and END
10. Graph compilation
11. Simple stateful graph
12. Loops and iterations
13. Human-in-the-loop
14. Checkpoints and persistence
15. Memory and threads
16. Tool-calling workflow
17. Agentic LangGraph workflow
18. RAG with LangGraph
19. Self-corrective RAG
20. Multi-agent graphs
21. Error handling and retry
22. Debugging and observability
23. Production considerations
24. Mini LangGraph workflow
25. Real LangGraph setup reference

## Key Mental Model

**State + Nodes + Edges + Conditional Routing = Graph Workflow**

LangGraph is especially useful when an LLM application needs explicit control over state, branching, loops, retries, persistence, or human approval.

## Important

The first examples are dependency-light simulations so the graph concepts are clear before using the actual package.

`25_Real_LangGraph_Setup_Reference.py` contains a real setup pattern. Install the required packages and adapt the model/provider layer for your application.

## GitHub Placement

```text
09--GENERATIVE AI/
└── 08--LangGraph/
```

## Prerequisite

Recommended previous folders:

```text
06--RAG/
07--LangChain/
```
