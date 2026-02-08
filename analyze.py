import pandas as pd

df = pd.read_csv("books_data.csv", encoding="utf-8")

# Clean price column (remove £ and weird characters)
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

print("Top 5 Most Expensive Books:")
print(df.sort_values("price", ascending=False).head())

print("\nAverage Price:")
print(df["price"].mean())

print("\nRating Distribution:")
print(df["rating"].value_counts())
