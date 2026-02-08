import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/"

product_list = []

response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p")["class"][1]  # e.g. "Three"
    
    product_list.append({
        "title": title,
        "price": price,
        "rating": rating
    })

df = pd.DataFrame(product_list)
df.to_csv("books_data.csv", index=False)

print("Scraped and saved:", df.shape)
