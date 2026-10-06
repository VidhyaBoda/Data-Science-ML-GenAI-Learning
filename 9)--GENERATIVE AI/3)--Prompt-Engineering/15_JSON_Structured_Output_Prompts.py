"""15 - JSON structured-output prompting"""

schema = {
    "customer_id": "string",
    "sentiment": "positive | neutral | negative",
    "priority": "low | medium | high",
    "reason": "string"
}

prompt = f"""
Extract customer feedback into exactly one JSON object.

Required schema:
{schema}

Rules:
- Do not add fields.
- Use null when the required value is unavailable.
- Do not wrap the JSON in Markdown.
"""

print(prompt)
