-- Write your PostgreSQL query statement below
WITH T
AS (SELECT DISTINCT o1.customer_id FROM orders o1
JOIN orders o2
ON o1.product_name = 'A' and o2.product_name = 'B' and o1.customer_id = o2.customer_id),
W AS
(SELECT * FROM T WHERE T.customer_id NOT IN( SELECT customer_id FROM orders WHERE product_name = 'C'))
SELECT c.customer_id, c.customer_name FROM customers c
JOIN W ON c.customer_id = W.customer_id
