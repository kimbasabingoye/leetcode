-- Write your PostgreSQL query statement below
WITH P AS
(SELECT product_id, SUM(unit) as unit
FROM orders
WHERE order_date >= '2020-02-01' AND order_date < '2020-03-01'
GROUP BY product_id
HAVING SUM(unit) >= 100)
SELECT product_name, p.unit FROM products JOIN p ON p.product_id = products.product_id
