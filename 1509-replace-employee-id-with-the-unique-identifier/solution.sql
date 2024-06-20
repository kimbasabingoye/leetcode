-- Write your PostgreSQL query statement below
select eu.unique_id, e.name from employees e LEFT join employeeuni eu on e.id = eu.id 
