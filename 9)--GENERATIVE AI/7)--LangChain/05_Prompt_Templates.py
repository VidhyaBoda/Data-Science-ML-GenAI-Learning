# 05 - Prompt Templates

template = """You are a {role}.
Explain {topic} for a {audience}.
Keep the explanation {style}."""

prompt = template.format(
    role="technical mentor",
    topic="LangChain",
    audience="beginner",
    style="simple and practical"
)

print(prompt)
