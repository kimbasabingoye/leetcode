# Write your MySQL query statement below
SELECT project_id, employee_id
FROM (
    SELECT
    project_id, e.employee_id,
    RANK() OVER(PARTITION BY project_id ORDER BY experience_years DESC) as rnk
    FROM project p
    JOIN employee e ON p.employee_id = e.employee_id
) T
WHERE rnk = 1
