"""18 - Common prompt failures and fixes"""

failures = {
    "Too vague": "Define the task, context and expected output.",
    "Missing context": "Supply the relevant facts or retrieve them.",
    "Conflicting instructions": "Remove contradictions and define priority clearly.",
    "Uncontrolled output": "Specify a schema, length or formatting contract.",
    "Unsupported facts": "Require grounding and an explicit missing-information behavior.",
    "Prompt too large": "Remove unnecessary context and use retrieval/chunking where appropriate.",
}

for failure, fix in failures.items():
    print(f"Failure: {failure}")
    print(f"Fix: {fix}\n")
