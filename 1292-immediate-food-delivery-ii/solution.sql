WITH t AS
(SELECT customer_id, MIN(order_date) AS first_order_date
FROM delivery
GROUP BY customer_id),
S AS
(SELECT t.customer_id, t.first_order_date, d.customer_pref_delivery_date
FROM t JOIN delivery d
ON t.customer_id = d.customer_id AND t.first_order_date = d.order_date)
SELECT ROUND(AVG(
    CASE WHEN customer_pref_delivery_date = first_order_date THEN 1.0 ELSE 0 END
)*100, 2) AS immediate_percentage
FROM S
