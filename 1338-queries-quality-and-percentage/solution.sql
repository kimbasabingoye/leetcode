-- Write your PostgreSQL query statement below
SELECT query_name,
ROUND(AVG(rating/CAST(position AS DECIMAL)), 2) AS quality,
ROUND(avg(CASE WHEN rating < 3 THEN 1 ELSE 0 END)*100, 2) as poor_query_percentage  from queries where query_name IS NOT NULL GROUP BY query_name
