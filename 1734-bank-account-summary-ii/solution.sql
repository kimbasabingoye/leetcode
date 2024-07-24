# Write your MySQL query statement below

SELECT name as NAME, SUM(amount) as BALANCE
FROM users u
JOIN transactions t
ON u.account = t.account
GROUP BY t.account
HAVING SUM(amount) > 10000
