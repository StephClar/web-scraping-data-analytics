import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "books_data.csv")
CHARTS_DIR = os.path.join(BASE_DIR, "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH, encoding="utf-8")

# Clean price
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# Rating conversion
rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
df["rating_num"] = df["rating"].map(rating_map)

# ---------------- STATISTICS ----------------
stats = df["price"].describe()
print("\n📊 Price Statistics:")
print(stats)

print("\n📊 Rating Statistics:")
print(df["rating_num"].describe())

# ---------------- VISUALIZATIONS ----------------

# Price vs Rating
plt.figure()
sns.scatterplot(data=df, x="rating_num", y="price")
plt.title("Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.savefig(os.path.join(CHARTS_DIR, "price_vs_rating.png"))
plt.close()

# Boxplot (Outliers)
plt.figure()
sns.boxplot(x=df["price"])
plt.title("Book Price Outliers")
plt.savefig(os.path.join(CHARTS_DIR, "boxplot_price.png"))
plt.close()

# Correlation Heatmap
plt.figure()
sns.heatmap(df[["price", "rating_num"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig(os.path.join(CHARTS_DIR, "correlation_heatmap.png"))
plt.close()

print("\n✅ Advanced analysis completed. Charts saved.")
