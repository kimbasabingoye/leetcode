WITH t as 
(SELECT s.user_id, 
       CASE 
           WHEN c.action = 'confirmed' THEN 1 
           ELSE 0 
       END as confirmation
FROM signups s
LEFT JOIN confirmations c
ON s.user_id = c.user_id)
SELECT t.user_id, ROUND(AVG(confirmation), 2) as confirmation_rate
FROM t
GROUP BY user_id

