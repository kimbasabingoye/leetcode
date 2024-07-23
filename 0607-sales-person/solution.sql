# Write your MySQL query statement below

SELECT s.name
FROM orders o
RIGHT JOIN salesperson s
ON o.sales_id = s.sales_id
GROUP BY s.sales_id
HAVING SUM(
    CASE
        WHEN o.com_id = (SELECT com_id FROM company c WHERE c.name='RED') THEN 1
        ELSE 0
    END
) = 0
