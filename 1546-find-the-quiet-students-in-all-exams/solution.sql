# Write your MySQL query statement below
WITH T AS
    (SELECT exam_id,
    MIN(score) as lowest_score,
    MAX(score) as highest_score
    FROM exam
    GROUP BY exam_id),
S AS
    (
        SELECT DISTINCT student_id 
        FROM T JOIN exam e ON T.exam_id = e.exam_id AND (score = lowest_score OR score = highest_score)
    )
SELECT s.student_id, s.student_name
FROM student s
WHERE student_id NOT IN (SELECT student_id FROM S) AND student_id IN (SELECT student_id FROM exam)
ORDER BY student_id
