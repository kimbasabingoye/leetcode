-- Write your PostgreSQL query statement below
WITH T AS
(SELECT u.id, COALESCE(SUM(distance), 0) as travelled_distance FROM users u LEFT JOIN rides r ON u.id = r.user_id
GROUP BY u.id)
SELECT u.name, t.travelled_distance FROM users u JOIN t ON u.id = t.id
ORDER BY travelled_distance DESC, name ASC
