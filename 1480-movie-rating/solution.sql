WITH feb_2020_rating AS
(
    SELECT * FROM movierating m WHERE m.created_at >= '2020-02-01' AND m.created_at < '2020-03-01' 
),
S AS (SELECT movie_id, AVG(rating) as avg_rating
FROM feb_2020_rating
GROUP BY movie_id),
R1 AS
(SELECT title as results FROM S JOIN movies m ON S.movie_id = m.movie_id
ORDER BY  avg_rating DESC, title ASC LIMIT 1),
T2 AS
(SELECT user_id, COUNT(user_id) as movie_count
FROM movierating
GROUP BY user_id),
R2 AS
(SELECT name as results FROM t2
JOIN users u ON t2.user_id = u.user_id
ORDER BY movie_count DESC, name ASC LIMIT 1)
SELECT * FROM R2
UNION ALL
SELECT * FROM R1


