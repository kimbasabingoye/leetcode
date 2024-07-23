# Write your MySQL query statement below
WITH T AS
(SELECT
host_team as team_id,
CASE
    WHEN host_goals > guest_goals THEN 3
    WHEN host_goals = guest_goals THEN 1
    ELSE 0
END AS points
FROM matches),
S AS(
    SELECT
        guest_team as team_id,
        CASE
            WHEN host_goals < guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS points
    FROM matches
),
W AS (SELECT * FROM T
UNION ALL
SELECT * FROM S)
SELECT 
te.team_id,
te.team_name,
COALESCE (SUM(points), 0) as num_points
FROM teams te
LEFT JOIN W ON te.team_id = W.team_id
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC
