SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    activity
WHERE 
    activity_date >= DATE '2019-07-27' - INTERVAL '29' DAY 
    AND activity_date <= DATE '2019-07-27'
GROUP BY 
    activity_date
ORDER BY 
    activity_date;

