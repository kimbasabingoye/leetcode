# Write your MySQL query statement below
SELECT player_id, device_id FROM
    (SELECT
    player_id, device_id,
    RANK() OVER (PARTITION BY player_id ORDER BY event_date ASC) as rnk 
    FROM activity
    ) T WHERE rnk =1
