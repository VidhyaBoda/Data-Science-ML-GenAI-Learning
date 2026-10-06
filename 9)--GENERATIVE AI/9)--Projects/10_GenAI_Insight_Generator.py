# Dependency-free simulation of a GenAI insight layer.
metrics = {
    "revenue_growth": 18.4,
    "repeat_customer_rate": 42.0,
    "top_category": "Technology"
}

def generate_insight(m):
    return (
        f"Revenue increased by {m['revenue_growth']:.1f}%. "
        f"Repeat-customer rate is {m['repeat_customer_rate']:.1f}%. "
        f"{m['top_category']} is the leading category. "
        "Prioritize retention campaigns and investigate drivers of category growth."
    )

print(generate_insight(metrics))
