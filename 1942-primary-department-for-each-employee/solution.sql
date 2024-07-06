-- Write your PostgreSQL query statement below
WITH employee_with_one_dept AS
(SELECT employee_id FROM employee
GROUP BY employee_id
HAVING COUNT(employee_id) = 1),
S AS
(SELECT e.employee_id, e.department_id FROM employee e
JOIN employee_with_one_dept e2 ON e.employee_id = e2.employee_id)
SELECT * FROM S
UNION SELECT employee_id, department_id FROM employee e WHERE primary_flag = 'Y'

