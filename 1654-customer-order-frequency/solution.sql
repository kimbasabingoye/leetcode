WITH T AS
(SELECT
order_id, customer_id, o.product_id, EXTRACT(YEAR_MONTH FROM order_date) order_date, SUM(quantity * price) as cost
FROM orders o
JOIN product p ON o.product_id = p.product_id 
WHERE EXTRACT(YEAR_MONTH FROM order_date) IN ('202006', '202007')
GROUP BY customer_id, EXTRACT(YEAR_MONTH FROM order_date))
SELECT t.customer_id, name FROM T
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY t.customer_id
HAVING SUM(
    CASE WHEN cost >= 100 THEN 1
         ELSE 0
    END
) = 2

