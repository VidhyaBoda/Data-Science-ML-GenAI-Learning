# 22 - Production Practices

practices = {
    "configuration": "Keep model/provider settings configurable.",
    "security": "Validate tools, credentials, and retrieved content.",
    "observability": "Track latency, errors, retrieval results, and model usage.",
    "evaluation": "Test retrieval and answer quality with representative datasets.",
    "cost": "Control token usage, model selection, caching, and unnecessary calls.",
    "versioning": "Pin important dependencies and review framework changes.",
    "testing": "Test individual components and complete chains."
}

for key, value in practices.items():
    print(f"{key}: {value}")
