# Write your MySQL query statement below
SELECT transaction_id 
FROM (
    SELECT transaction_id ,
    RANK() OVER(PARTITION BY day ORDER BY amount DESC) as rnk
    FROM transactions
) t WHERE rnk = 1
ORDER BY transaction_id 
