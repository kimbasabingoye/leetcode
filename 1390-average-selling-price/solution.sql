-- Write your PostgreSQL query statement below
WITH t AS
(SELECT p.product_id, p.price, COALESCE(u.units, 0) as units
FROM prices p 
LEFT JOIN unitssold u ON p.product_id = u.product_id and u.purchase_date BETWEEN p.start_date and p.end_date)
SELECT t.product_id, 
CASE
    WHEN SUM(t.units) = 0 THEN 0
    ELSE CAST(SUM(CAST(t.price * t.units AS DECIMAL(7,2)))/SUM(t.units)as DECIMAL(7, 2))
END as average_price
FROM t
GROUP BY t.product_id
