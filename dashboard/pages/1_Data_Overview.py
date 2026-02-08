import streamlit as st
import pandas as pd
import os

st.title("Dataset Overview")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "books_data.csv")

df = pd.read_csv(DATA_PATH, encoding="utf-8")

st.subheader("First 10 Records")
st.dataframe(df.head(10))

st.subheader("Dataset Shape")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.subheader("🧾 Raw Dataset Column Types")
st.write(df.dtypes)

# Clean price for preview
clean_df = df.copy()
clean_df["price"] = (
    clean_df["price"]
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
clean_df["rating_num"] = clean_df["rating"].map(rating_map)

st.subheader("✅ Cleaned Dataset Column Types")
st.write(clean_df[["price", "rating_num"]].dtypes)
