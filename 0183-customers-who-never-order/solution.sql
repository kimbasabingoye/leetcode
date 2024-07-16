-- Write your PostgreSQL query statement below
--SELECT name as customers FROM customers
--WHERE id not in (select customerID FROM orders)
SELECT name as customers 
FROM Customers
LEFT JOIN Orders ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId IS NULL
