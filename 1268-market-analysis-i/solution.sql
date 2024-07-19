-- Write your PostgreSQL query statement below
SELECT t.user_id as buyer_id, join_date, t.orders_in_2019 FROM users u1
JOIN (SELECT user_id, COUNT(order_id) as orders_in_2019 FROM users u
LEFT JOIN orders o ON u.user_id = o.buyer_id AND EXTRACT(YEAR FROM order_date) = '2019'
GROUP BY user_id) as t ON u1.user_id = t.user_id
