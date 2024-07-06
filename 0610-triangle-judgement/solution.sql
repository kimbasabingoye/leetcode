-- Write your PostgreSQL query statement below
-- AB = x
-- AC = y
-- BC = z
-- abs(AC-CB) <= AB <= AC + CB

SELECT x, y, z,
CASE
    WHEN x+y > z AND x+z > y AND y+z>x 
        THEN 'Yes'
    ELSE 'No'
END AS triangle
FROM triangle

