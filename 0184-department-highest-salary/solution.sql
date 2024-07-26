# Write your MySQL query statement below
WITH T AS (SELECT
d.name as Department,
e.name as Employee,
e.salary as Salary,
RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) as rnk
FROM employee e JOIN department d ON e.departmentId = d.id)
SELECT Department, Employee, Salary FROM T
WHERE rnk = 1
