"""09 - Prompt templates"""

template = """
You are a {role}.
Task: {task}
Context: {context}
Constraints:
{constraints}
Output format: {output_format}
"""

values = {
    "role": "Data Analyst",
    "task": "Explain the KPI trend",
    "context": "Monthly revenue increased for three consecutive months.",
    "constraints": "- Be concise\n- Mention possible drivers\n- Do not invent facts",
    "output_format": "3 bullet points",
}

prompt = template.format(**values)
print(prompt)
