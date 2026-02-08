import pandas as pd

df = pd.read_csv("books_data.csv", encoding="utf-8")

# Clean price
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating_num"] = df["rating"].map(rating_map)

print("Total Books:", len(df))
print("\nAverage Price:", df["price"].mean())
print("\nTop 10 Expensive Books:")
print(df.sort_values("price", ascending=False).head(10))
