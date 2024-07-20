-- Write your PostgreSQL query statement below
WITH T AS
(SELECT customer_number, COUNT(customer_number) as cnt_order
FROM orders
GROUP BY customer_number)
SELECT customer_number FROM T
WHERE cnt_order = (SELECT MAX(cnt_order) FROM T)
