-- Write your PostgreSQL query statement below
DELETE FROM person p where p.id NOT IN
(SELECT
MIN(id) as id
FROM person
GROUP BY email)
