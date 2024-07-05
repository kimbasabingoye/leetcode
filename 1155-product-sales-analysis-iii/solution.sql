-- Write your PostgreSQL query statement below
WITH t AS
(SELECT product_id, MIN(year) first_year
FROM sales
GROUP BY product_id)
SELECT s.product_id, t.first_year, s.quantity, s.price
FROM sales s
JOIN t ON s.product_id = t.product_id AND s.year = t.first_year 
