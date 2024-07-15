-- Write your PostgreSQL query statement below
WITH T AS
(SELECT requester_id as id
FROM requestaccepted
UNION ALL
SELECT accepter_id as id
FROM requestaccepted
)
SELECT id, COUNT(id) as  num FROM T
GROUP BY id
ORDER BY num DESC
LIMIT 1
