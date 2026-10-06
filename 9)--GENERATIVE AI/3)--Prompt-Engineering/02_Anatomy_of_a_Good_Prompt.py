"""02 - Anatomy of a good prompt"""

prompt = {
    "role": "You are a data analyst.",
    "task": "Analyze the sales data.",
    "context": "The dataset contains order date, product, region and revenue.",
    "constraints": "Use concise business language and identify the top 3 insights.",
    "output_format": "Return a numbered list with insight, evidence and business action."
}

for section, content in prompt.items():
    print(f"{section.upper()}: {content}")
