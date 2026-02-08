import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 51):  # 50 pages
    print(f"Scraping page {page}...")
    
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]

        all_books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

df = pd.DataFrame(all_books)
df.to_csv("books_data.csv", index=False, encoding="utf-8")

print("Scraping completed!")
print("Total books scraped:", len(df))
