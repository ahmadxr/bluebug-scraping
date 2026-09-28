# Notes

- Rating isn't text, it's a class like `star-rating Three`, so I mapped the words to 1-5.
- Price had the pound sign plus some encoding noise, stripping it took a couple of tries.
- Book links are relative (`../../../...`), had to join them to full urls.
- `in_stock` check took longest to trust - first 100 are all in stock, so I re-checked page html to make sure the false case works.
- If it blocked me after 50 requests I'd slow down, reuse one session with normal headers, save each page to disk, retry with backoff, and stop hammering it.
