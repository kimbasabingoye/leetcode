-- Write your PostgreSQL query statement below

WITH t as
(select managerId, count(*) as count_direct_report from employee
group by managerId having count(*) >= 5)
select name from employee e
JOIN t ON e.id = t.managerId
