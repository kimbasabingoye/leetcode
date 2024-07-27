# Write your MySQL query statement below
SELECT seat_id 
FROM cinema c1
WHERE c1.free = 1 AND 1 IN (
    SELECT free FROM cinema c2 WHERE c2.seat_id = c1.seat_id + 1 OR c2.seat_id = c1.seat_id - 1
) 

