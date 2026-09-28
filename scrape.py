import csv
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"
LIST_URL = BASE + "catalogue/page-{}.html"

RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def get_soup(page):
    r = requests.get(LIST_URL.format(page), timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def parse_book(tag):
    a = tag.h3.a
    title = a.get("title", "").strip()

    price_txt = tag.find("p", class_="price_color").get_text().strip()
    price = float(price_txt.replace("\u00a3", "").replace("\u00c2", ""))

    rating_cls = tag.find("p", class_="star-rating").get("class", [])
    rating_word = [c for c in rating_cls if c != "star-rating"][0]
    rating = RATINGS.get(rating_word, 0)

    avail = tag.find("p", class_="instock").get_text().lower()
    in_stock = "in stock" in avail

    url = urljoin(BASE + "catalogue/", a.get("href", ""))

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "in_stock": str(in_stock).lower(),
        "url": url,
    }


def main():
    books = []
    for page in range(1, 6):
        soup = get_soup(page)
        for tag in soup.select("article.product_pod"):
            books.append(parse_book(tag))
            if len(books) >= 100:
                break
        print(f"page {page}: {len(books)} so far")
        time.sleep(0.5)
        if len(books) >= 100:
            break

    with open("books.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["title", "price", "rating", "in_stock", "url"])
        w.writeheader()
        w.writerows(books[:100])

    print(f"wrote {min(len(books), 100)} books to books.csv")


if __name__ == "__main__":
    main()
