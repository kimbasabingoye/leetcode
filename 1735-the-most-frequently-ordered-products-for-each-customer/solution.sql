# Write your MySQL query statement below
WITH T AS
(SELECT
    c.customer_id, p.product_id, product_name,
    COUNT(*) as cnt
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN products p ON o.product_id = p.product_id
GROUP BY customer_id, product_id)
SELECT customer_id, product_id, product_name
FROM T WHERE cnt = (SELECT MAX(cnt) FROM T as t1 WHERE t.customer_id = t1.customer_id) 
