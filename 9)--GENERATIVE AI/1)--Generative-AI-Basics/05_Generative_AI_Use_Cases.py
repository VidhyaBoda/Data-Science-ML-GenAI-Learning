"""
05 - Generative AI Industry Use Cases

Learning objective:
Connect Generative AI concepts with real-world applications.
"""

use_cases = {
    "Data Analytics": [
        "Generate SQL queries",
        "Explain analytical results",
        "Create documentation",
        "Assist with data-cleaning logic",
    ],
    "Software Engineering": [
        "Generate code",
        "Explain code",
        "Write unit-test drafts",
        "Assist debugging",
    ],
    "Business": [
        "Summarize reports",
        "Draft business documents",
        "Extract information from text",
        "Create customer-support responses",
    ],
    "Knowledge Systems": [
        "Question answering",
        "Document summarization",
        "RAG-based enterprise assistants",
    ],
}

for domain, applications in use_cases.items():
    print(f"\n{domain}")
    for application in applications:
        print(f"  - {application}")
