# Before calling a portfolio project production-ready.
checks = [
    "Secrets stored outside source code",
    "Input validation",
    "Error handling",
    "Logging",
    "Evaluation dataset",
    "Latency and cost awareness",
    "Data privacy review",
    "Reproducible setup",
    "Clear README",
]
for i, item in enumerate(checks, 1):
    print(f"{i:02}. {item}")
