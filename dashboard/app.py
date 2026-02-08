import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# --------- Load Data ---------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "books_data.csv")

df = pd.read_csv(DATA_PATH, encoding="utf-8")

df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
df["rating_num"] = df["rating"].map(rating_map)

# --------- Streamlit UI ---------
st.set_page_config(page_title="Book Analytics Dashboard", layout="wide")
st.title("Book Data Analytics & AIML Dashboard")

# --------- Show Data ---------
st.subheader("Dataset Preview")
st.dataframe(df.head(20))

# --------- Charts ---------
st.subheader("Price Distribution")
fig1, ax1 = plt.subplots()
ax1.hist(df["price"], bins=20)
st.pyplot(fig1)

st.subheader("Rating Distribution")
fig2, ax2 = plt.subplots()
df["rating"].value_counts().plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# --------- ML: Price Prediction ---------
st.subheader("💰 Book Price Prediction")

X = df[["rating_num"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

rating_input = st.slider("Select Rating", 1, 5, 3)
predicted_price = model.predict([[rating_input]])[0]

st.success(f"Predicted Price: £{predicted_price:.2f}")

# --------- Recommendation System ---------
st.subheader("🤖 Book Recommendation System")

scaler = MinMaxScaler()
features = scaler.fit_transform(df[["price", "rating_num"]])
similarity = cosine_similarity(features)

book_index = st.selectbox("Choose a book", df.index, format_func=lambda x: df.iloc[x]["title"])

if st.button("Recommend Similar Books"):
    scores = list(enumerate(similarity[book_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    st.write("Recommended Books:")
    for idx, score in scores:
        st.write(f"- {df.iloc[idx]['title']} (Similarity: {score:.2f})")
