# Write your MySQL query statement below
WITH T AS
(SELECT student_id, course_id, grade,
RANK() OVER(PARTITION BY student_id ORDER BY grade DESC, course_id ASC) as rn
FROM enrollments e)
SELECT student_id, course_id, grade
FROM T WHERE rn = 1

