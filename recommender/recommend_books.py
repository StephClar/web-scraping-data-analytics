import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "books_data.csv")

# Load data
df = pd.read_csv(DATA_PATH, encoding="utf-8")

# Clean price
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# Convert rating to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["rating_num"] = df["rating"].map(rating_map)

# Scale features
scaler = MinMaxScaler()
features = scaler.fit_transform(df[["price", "rating_num"]])

# Similarity matrix
similarity_matrix = cosine_similarity(features)

def recommend_books(book_index, top_n=5):
    similarity_scores = list(enumerate(similarity_matrix[book_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    recommended = similarity_scores[1:top_n+1]
    
    print("\n📚 Recommended Books:")
    for idx, score in recommended:
        print(f"- {df.iloc[idx]['title']} (Similarity: {score:.2f})")

# Example usage
print("Selected Book:")
print(df.iloc[0]["title"])

recommend_books(book_index=0)
