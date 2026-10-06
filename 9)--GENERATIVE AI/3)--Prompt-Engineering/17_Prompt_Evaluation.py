"""17 - Prompt evaluation"""

evaluation_criteria = {
    "Correctness": "Does the output satisfy the task?",
    "Groundedness": "Is the output supported by supplied information?",
    "Format compliance": "Does it follow the requested schema?",
    "Consistency": "Does it behave reliably across representative inputs?",
    "Safety": "Does it avoid unacceptable or unsafe behavior?",
    "Usefulness": "Does the output help the intended user complete the task?",
}

for criterion, question in evaluation_criteria.items():
    print(f"{criterion}: {question}")

print("\nProfessional prompting requires evaluation, not just writing a clever prompt once.")
