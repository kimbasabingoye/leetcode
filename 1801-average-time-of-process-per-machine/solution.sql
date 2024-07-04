-- Write your PostgreSQL query statement below
WITH t AS 
(SELECT machine_id, activity_type, SUM(timestamp) AS total_start
FROM activity 
GROUP BY machine_id, activity_type),
s AS
(SELECT machine_id, 
CASE 
    WHEN activity_type = 'start' 
        THEN -total_start
        ELSE total_start
END AS total
FROM t),
W AS
(SELECT machine_id, SUM(total)/(SELECT COUNT(DISTINCT process_id) FROM activity) AS processing_time
FROM S
GROUP BY machine_id)
SELECT machine_id, round(processing_time::numeric, 3) as processing_time FROM w

    
