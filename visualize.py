import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)

df = pd.read_csv("books_data.csv", encoding="utf-8")

# Clean price column
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

# 📊 Price Distribution
plt.figure()
plt.hist(df["price"], bins=20)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.savefig("charts/price_distribution.png")
plt.close()

# 📊 Rating Distribution
df["rating"].value_counts().plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.savefig("charts/rating_distribution.png")
plt.close()

print("Charts saved in 'charts/' folder")
