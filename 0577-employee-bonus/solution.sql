-- Write your PostgreSQL query statement below
SELECT name, bonus from Employee e LEFT JOIN bonus b ON e.empId = b.empId where b.bonus < 1000 or b.bonus is null

--SELECT * from Employee e LEFT JOIN bonus b ON e.empId = b.empId
