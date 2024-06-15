# Write your MySQL query statement below
SELECT name, bonus FROM employee e left join bonus b on e.empId = b.empId where b.bonus < 1000 or b.bonus IS NULL;
