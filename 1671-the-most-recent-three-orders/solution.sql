# Write your MySQL query statement below
SELECT customer_name, customer_id, order_id, order_date
FROM (
    SELECT c.name as customer_name, c.customer_id, order_id, order_date,
    RANK() OVER(PARTITION BY customer_id ORDER BY order_date DESC) as rnk
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
) T WHERE rnk <= 3
ORDER BY customer_name, customer_id, order_date DESC
