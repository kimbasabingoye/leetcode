# Write your MySQL query statement below
SELECT
DISTINCT(title) as title
FROM TVProgram t JOIN content c
ON t.content_id = c.content_id
WHERE Kids_content = 'Y' AND EXTRACT(YEAR_MONTH FROM program_date) = '202006' AND content_type = 'Movies'

