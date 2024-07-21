# Write your MySQL query statement below
SELECT
c.customer_id,
c.customer_name
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY o.customer_id
HAVING SUM(o.product_name='A') > 0 AND SUM(o.product_name='B') > 0 and SUM(o.product_name='C') = 0
