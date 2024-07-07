-- Write your PostgreSQL query statement below

WITH t AS
(SELECT product_id, MAX(change_date) as change_date
FROM products
WHERE change_date <= '2019-08-16'
GROUP BY product_id)
SELECT t.product_id, p.new_price as price
FROM t JOIN products p ON t.product_id = p.product_id AND t.change_date = p.change_date
UNION ALL
SELECT product_id, '10' as price
FROM products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'
