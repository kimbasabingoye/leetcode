-- Write your PostgreSQL query statement below
SELECT customer_id, count(*) as count_no_trans from visits v where v.visit_id not in (select visit_id from transactions) GROUP BY customer_id
