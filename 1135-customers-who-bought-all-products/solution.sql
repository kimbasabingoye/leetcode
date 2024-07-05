-- Write your PostgreSQL query statement below
WITH t AS
(SELECT customer_id, COUNT(DISTINCT product_key) as num_product_bought
FROM customer
GROUP BY customer_id)
SELECT customer_id FROM t
WHERE num_product_bought = (SELECT COUNT(DISTINCT product_key) FROM product)
