-- Write your PostgreSQL query statement below
WITH S AS
(SELECT reports_to, COUNT(employee_id) as reports_count, ROUND(AVG(age)) AS average_age FROM employees
WHERE reports_to IS NOT NULL
GROUP BY reports_to)
SELECT employee_id, name, S.reports_count, S.average_age FROM employees e
JOIN S ON e.employee_id = S.reports_to
ORDER BY employee_id
