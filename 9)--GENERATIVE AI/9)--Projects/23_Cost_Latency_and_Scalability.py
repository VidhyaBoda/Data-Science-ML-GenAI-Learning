# Simple planning model for GenAI operations.
requests_per_day = 500
avg_tokens_per_request = 1200
estimated_tokens_per_day = requests_per_day * avg_tokens_per_request

print("Requests/day:", requests_per_day)
print("Estimated input+output tokens/day:", estimated_tokens_per_day)
print("Design implication: cache repeated queries and control context size where possible.")
