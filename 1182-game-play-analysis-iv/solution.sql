-- Write your PostgreSQL query statement below
WITH t AS
(
    SELECT player_id, MIN(event_date) first_login
    FROM activity GROUP BY player_id
)
SELECT ROUND(COUNT(*)*1.0/(SELECT COUNT(DISTINCT player_id) FROM activity), 2) AS fraction
FROM activity a 
JOIN t ON t.first_login + 1 = a.event_date AND t.player_id = a.player_id 
