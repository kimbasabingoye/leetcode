-- Write your PostgreSQL query statement below
SELECT name as "Customers" FROM customers c
WHERE c.id NOT IN (SELECT customerId as id FROM orders)
