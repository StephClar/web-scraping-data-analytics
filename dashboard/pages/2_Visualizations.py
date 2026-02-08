import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("Visualizations")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "books_data.csv")

df = pd.read_csv(DATA_PATH, encoding="utf-8")

# Clean price
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# Rating mapping
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["rating_num"] = df["rating"].map(rating_map)

st.subheader("Price Distribution")
fig, ax = plt.subplots()
ax.hist(df["price"], bins=20)
ax.set_xlabel("Price")
ax.set_ylabel("Count")
st.pyplot(fig)

st.subheader("Price vs Rating")
fig, ax = plt.subplots()
ax.scatter(df["rating_num"], df["price"])
ax.set_xlabel("Rating")
ax.set_ylabel("Price")
st.pyplot(fig)
