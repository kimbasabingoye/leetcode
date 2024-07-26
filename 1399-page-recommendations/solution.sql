# Write your MySQL query statement below
WITH user_1_friends AS(
    SELECT GREATEST(user1_id, user2_id) as friend_id
    FROM friendship
    WHERE LEAST(user1_id, user2_id) = 1
)
SELECT DISTINCT(page_id) as recommended_page
FROM user_1_friends u
JOIN likes l
ON u.friend_id = l.user_id
WHERE page_id NOT IN (SELECT page_id FROM likes where user_id = 1)
