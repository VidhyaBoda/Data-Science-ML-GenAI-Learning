"""12 - Summarization and extraction prompts"""

text = """
Customer retention improved after the onboarding process was shortened.
The report also notes that enterprise customers had the highest renewal rate.
"""

summary_prompt = f"""
Summarize the following text in two bullet points.

<document>
{text.strip()}
</document>
"""

extraction_prompt = f"""
Extract:
- retention change
- customer segment with highest renewal rate

Return only the extracted facts.

<document>
{text.strip()}
</document>
"""

print("SUMMARY PROMPT:\n", summary_prompt)
print("\nEXTRACTION PROMPT:\n", extraction_prompt)
