import streamlit as st
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

st.title("Price Prediction")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "books_data.csv")

df = pd.read_csv(DATA_PATH, encoding="utf-8")

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

X = df[["rating_num"]]
y = df["price"]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

pipeline.fit(X, y)

rating = st.slider("Select Book Rating", 1, 5, 3)

predicted_price = pipeline.predict([[rating]])

st.success(f"Predicted Price: £{predicted_price[0]:.2f}")
