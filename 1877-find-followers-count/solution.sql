-- Write your PostgreSQL query statement below
SELECT user_id, COUNT(*) as followers_count FROM followers GROUP By user_id ORDER BY user_id ASC
