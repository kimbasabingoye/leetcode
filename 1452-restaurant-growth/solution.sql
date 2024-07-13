-- Write your PostgreSQL query statement below
WITH T AS
(SELECT DISTINCT visited_on FROM customer WHERE visited_on >= (SELECT MIN(visited_on)+6 FROM customer)
ORDER BY visited_on)
SELECT t.visited_on, SUM(amount) as amount, ROUND(SUM(amount)/7.0, 2) as average_amount FROM T JOIN customer c ON c.visited_on BETWEEN t.visited_on - 6 AND t.visited_on
GROUP BY t.visited_on
ORDER BY t.visited_on
