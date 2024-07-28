# Write your MySQL query statement below
SELECT id,
CASE
    WHEN p_id IS NULL THEN 'Root'
    WHEN (SELECT COUNT(*) FROM tree t1 WHERE t1.p_id = t.id) >= 1 THEN 'Inner'
    ELSE 'Leaf'
END AS type
FROM tree t 
