"""16 - Basic LLM application architecture"""

architecture = [
    "User",
    "Application / API layer",
    "Prompt + conversation/context management",
    "Optional retrieval / tools",
    "LLM",
    "Post-processing / validation",
    "Response to user",
]

for i, component in enumerate(architecture, 1):
    arrow = " -> " if i < len(architecture) else ""
    print(f"{component}{arrow}", end="")

print("\n")
print("Production systems commonly add authentication, logging, monitoring,")
print("rate limiting, evaluation, safety controls and observability.")
