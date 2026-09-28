import csv
import sqlite3

con = sqlite3.connect("books.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS books")
cur.execute("""
CREATE TABLE books (
  title TEXT,
  price REAL,
  rating INTEGER,
  in_stock TEXT,
  url TEXT
)
""")

with open("books.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    cur.executemany(
        "INSERT INTO books VALUES (:title, :price, :rating, :in_stock, :url)",
        rows,
    )

con.commit()
print(f"loaded {len(rows)} rows")

print("\n-- 1. avg price per rating")
for r in cur.execute("SELECT rating, ROUND(AVG(price), 2), COUNT(*) FROM books GROUP BY rating ORDER BY rating"):
    print(r)

print("\n-- 2. top 5 most expensive rated 4 or 5")
for r in cur.execute("SELECT title, price, rating FROM books WHERE rating >= 4 ORDER BY price DESC LIMIT 5"):
    print(r)

print("\n-- 3. out of stock per rating")
for r in cur.execute("SELECT rating, COUNT(*) FROM books WHERE in_stock = 'false' GROUP BY rating ORDER BY rating"):
    print(r)
print("(no rows above = 0 out of stock)")

con.close()
