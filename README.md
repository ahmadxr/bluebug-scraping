# bluebug-scraping

# Results (100 books, pages 1-5)

## 1. Average price per rating

| rating | avg_price | n |
|---|---|---|
| 1 | 35.52 | 22 |
| 2 | 35.91 | 19 |
| 3 | 36.84 | 22 |
| 4 | 33.98 | 18 |
| 5 | 30.01 | 19 |

## 2. Top 5 most expensive, rating 4-5

| title | price | rating |
|---|---|---|
| The Death of Humanity: and the Case for Life | 58.11 | 4 |
| The Past Never Ends | 56.50 | 4 |
| Sapiens: A Brief History of Humankind | 54.23 | 5 |
| Scott Pilgrim's Precious Little Life (Scott Pilgrim #1) | 52.29 | 5 |
| Behind Closed Doors | 52.22 | 4 |

## 3. Out of stock per rating

No rows - 0 books out of stock in the first 100. All `in_stock` values are `true`.
The query used:

```sql
SELECT rating, COUNT(*) FROM books WHERE in_stock = 'false' GROUP BY rating;
```

How to run it yourself:

```
python scrape.py
python db.py
sqlite3 books.db < queries.sql
```


## Notes

- Rating is stored in the class name like star-rating Three, so I mapped the words to 1-5.
- Price came with a pound sign and some encoding bytes, cleaning that took a couple of tries.
- Book urls are relative, so I joined them to full catalogue links.
- The stock check took the longest to trust since the first 100 are all in stock and I had to recheck the html for the false case.
- If it blocked me after 50 requests I would slow down, use one session with normal headers, save pages to disk, and retry with backoff.
