-- Write your PostgreSQL query statement below
SELECT employee_id
FROM employees e
WHERE salary < 30000 AND manager_id NOT IN (SELECT employee_id FROM employees)
ORDER BY employee_id

