"""14 - SQL and Python prompt patterns"""

sql_prompt = """
You are a SQL analyst.
Given the supplied schema, write a query to calculate monthly revenue.
Requirements:
- Use explicit column names.
- Explain assumptions briefly.
- Do not invent tables or columns.
- Handle NULL revenue values appropriately.
"""

python_prompt = """
You are a Python data engineer.
Write a pandas transformation for the supplied DataFrame.
Requirements:
- Preserve the original DataFrame unless explicitly asked otherwise.
- Avoid chained assignment.
- Explain time and memory considerations when relevant.
- Include a small test example.
"""

print("SQL prompt pattern:\n", sql_prompt)
print("\nPython prompt pattern:\n", python_prompt)
