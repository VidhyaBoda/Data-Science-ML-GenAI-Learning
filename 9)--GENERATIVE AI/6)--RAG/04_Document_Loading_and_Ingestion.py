"""
04 - Document Loading and Ingestion
A dependency-free conceptual ingestion example.
"""

documents = [
    {"id": "doc_1", "text": "Company leave policy allows employees to apply for annual leave."},
    {"id": "doc_2", "text": "Employees should submit leave requests before the planned leave date."}
]

def ingest(records):
    cleaned = []
    for record in records:
        text = " ".join(record["text"].split())
        cleaned.append({"id": record["id"], "text": text})
    return cleaned

ingested = ingest(documents)

for item in ingested:
    print(item)
