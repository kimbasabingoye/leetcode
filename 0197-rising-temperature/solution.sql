-- Write your PostgreSQL query statement below
-- SELECT * FROM weather ORDER BY recordDate ASC;

SELECT id FROM weather w WHERE w.temperature > (SELECT temperature from weather s where w.recordDate = s.recordDate+1)

