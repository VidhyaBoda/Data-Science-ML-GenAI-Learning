# 20 - Structured Output

import json

output = {
    "topic": "LangChain",
    "difficulty": "beginner",
    "key_points": ["Models", "Prompts", "Retrievers", "Tools", "Agents"]
}

print(json.dumps(output, indent=2))
