-- 1. average price for each rating
SELECT rating, ROUND(AVG(price), 2) AS avg_price, COUNT(*) AS n
FROM books
GROUP BY rating
ORDER BY rating;

-- 2. 5 most expensive books rated 4 or 5
SELECT title, price, rating
FROM books
WHERE rating >= 4
ORDER BY price DESC
LIMIT 5;

-- 3. out of stock count per rating
SELECT rating, COUNT(*) AS out_of_stock
FROM books
WHERE in_stock = 'false'
GROUP BY rating
ORDER BY rating;
