# Write your MySQL query statement below
SELECT player_id, player_name, COUNT(*) as  grand_slams_count
FROM (
    SELECT player_id, player_name FROM
    players p JOIN championships c ON p.player_id = c.wimbledon
    UNION ALL
    SELECT player_id, player_name FROM
    players p JOIN championships c ON p.player_id = c.fr_open
    UNION ALL
    SELECT player_id, player_name FROM
    players p JOIN championships c ON p.player_id = c.us_open 
    UNION ALL
    SELECT player_id, player_name FROM
    players p JOIN championships c ON p.player_id = c.au_open
) T
GROUP BY player_name
