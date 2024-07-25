# Write your MySQL query statement below
WITH T AS
(SELECT employee_id
FROM employees e
WHERE employee_id NOT in (SELECT employee_id FROM salaries)),
S AS
(SELECT employee_id FROM salaries s
WHERE employee_id NOT IN (SELECT employee_id FROM employees)),
W AS (
    SELECT * FROM T  UNION ALL SELECT * FROM S)
SELECT * FROM W order by employee_id
