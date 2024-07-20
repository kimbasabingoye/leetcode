# Write your MySQL query statement below
WITH T AS
(
    SELECT
    id,
    name,
    salary,
    departmentId,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rn
    FROM employee
) #SELECT * FROM T
SELECT d.name as Department, T.name as Employee, T.salary as Salary
FROM T
JOIN department d
ON T.departmentId = d.id
WHERE rn <= 3
