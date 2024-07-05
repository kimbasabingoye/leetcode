-- Write your PostgreSQL query statement below
WITH t AS
(select num from mynumbers group by num having count(*) = 1)
SELECT MAX(num) as num FROM t
