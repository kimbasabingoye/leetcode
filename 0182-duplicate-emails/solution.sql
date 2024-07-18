# Write your MySQL query statement below
SELECT Email 
FROM person
WHERE email is not NULL
GROUP BY email
HAVING COUNT(email) > 1
