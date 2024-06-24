-- Write your PostgreSQL query statement below
WITH t AS
(SELECT contest_id, COUNT(*) as nb FROM register
GROUP By contest_id)
SELECT t.contest_id, ROUND((t.nb * 100.0)/(SELECT COUNT(*) FROM users), 2) as percentage
FROM t
ORDER BY percentage DESC, contest_id ASC
