import pandas as pd

df = pd.DataFrame({
    "customer_id": [1, 2, 3, 3],
    "revenue": [1200, 850, None, 900],
    "category": ["Tech", "Home", "Tech", "Tech"]
})

df = df.drop_duplicates().copy()
df["revenue"] = df["revenue"].fillna(df["revenue"].median())

print(df)
print("\nMissing values:\n", df.isna().sum())
