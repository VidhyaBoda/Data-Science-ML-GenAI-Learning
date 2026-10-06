import pandas as pd

df = pd.DataFrame({
    "category": ["Tech", "Tech", "Home", "Fashion", "Home"],
    "revenue": [1200, 900, 700, 500, 800]
})

category_revenue = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
print("Revenue by category:")
print(category_revenue)

print("\nTop category:", category_revenue.index[0])
print("Top revenue:", category_revenue.iloc[0])
