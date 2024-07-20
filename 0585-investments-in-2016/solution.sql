-- Write your PostgreSQL query statement below
WITH S AS
(
    SELECT pid
    FROM insurance
    GROUP BY CONCAT(lat, lon)
    HAVING COUNT(DISTINCT CONCAT(lat, lon)) = COUNT(CONCAT(lat, lon))
),
T AS
(
    SELECT pid FROM insurance
    WHERE tiv_2015 IN 
        (
            SELECT tiv_2015 FROM insurance
            GROUP BY tiv_2015
            HAVING COUNT(tiv_2015) > 1
        )
)
SELECT ROUND(SUM(tiv_2016), 2) as tiv_2016 FROM insurance i
JOIN (SELECT pid FROM t WHERE pid IN (SELECT * FROM s)) as w
ON i.pid = w.pid

