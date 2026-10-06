"""07 - Output format control"""

output_contract = {
    "format": "JSON",
    "fields": ["sentiment", "issue", "priority"],
    "rules": [
        "Use only the requested fields.",
        "Return one JSON object.",
        "Do not add explanatory text outside the object."
    ]
}

print("Desired output contract:")
for key, value in output_contract.items():
    print(f"{key}: {value}")
