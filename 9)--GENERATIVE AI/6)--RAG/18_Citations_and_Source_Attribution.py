"""
18 - Citations and Source Attribution
Keep source references alongside retrieved content.
"""

answer = {
    "text": "Employees can apply for annual leave through the HR portal.",
    "sources": [
        {
            "document": "leave_policy.md",
            "section": "Annual Leave",
            "chunk_id": "chunk_04"
        }
    ]
}

print("Answer:", answer["text"])
print("\nSources:")
for source in answer["sources"]:
    print(source)
