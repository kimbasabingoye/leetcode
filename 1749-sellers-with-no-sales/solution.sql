# Write your MySQL query statement below
SELECT seller_name
FROM seller s
LEFT JOIN orders o
ON s.seller_id = o.seller_id and EXTRACT(YEAR FROM sale_date) = '2020'
WHERE o.sale_date IS NULL
ORDER BY seller_name
