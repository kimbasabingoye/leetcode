# Write your MySQL query statement below
SELECT product_name, product_id, order_id, order_date
FROM ( 
    SELECT
    o.order_id, o.order_date, o.customer_id, o.product_id,
    p.product_name,
    DENSE_RANK() OVER(PARTITION BY o.product_id ORDER BY order_date DESC) as rnk
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
) AS S WHERE rnk = 1
ORDER BY product_name ASC, product_id ASC, order_id ASC
