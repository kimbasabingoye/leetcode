# Write your MySQL query statement below
SELECT 
LEAST(from_id, to_id) AS person1,
GREATEST(from_id, to_id) AS person2,
COUNT(*) as call_count,
SUM(duration) as total_duration
FROM calls
GROUP BY person1, person2
