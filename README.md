# bluebug-scraping

Scrape of the first 100 books from books.toscrape.com, pages 1 to 5. Output is in books.csv.

## SQL answers

Loaded books.csv into SQLite with db.py. Queries are in queries.sql.

1. Average price for each rating:

rating 1: 35.52 (22 books)
rating 2: 35.91 (19 books)
rating 3: 36.84 (22 books)
rating 4: 33.98 (18 books)
rating 5: 30.01 (19 books)

2. The 5 most expensive books rated 4 or 5:

The Death of Humanity: and the Case for Life - 58.11 - rating 4
The Past Never Ends - 56.50 - rating 4
Sapiens: A Brief History of Humankind - 54.23 - rating 5
Scott Pilgrim's Precious Little Life (Scott Pilgrim #1) - 52.29 - rating 5
Behind Closed Doors - 52.22 - rating 4

3. How many books are out of stock, per rating:

None. All 100 books are in stock, so the out of stock count is 0 for every rating.

## Notes

- Rating is stored in the class name like star-rating Three, so I mapped the words to 1-5.
- Price came with a pound sign and some encoding bytes, cleaning that took a couple of tries.
- Book urls are relative, so I joined them to full catalogue links.
- The stock check took the longest to trust since the first 100 are all in stock and I had to recheck the html for the false case.
- If it blocked me after 50 requests I would slow down, use one session with normal headers, save pages to disk, and retry with backoff.
