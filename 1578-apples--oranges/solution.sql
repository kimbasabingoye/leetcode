# Write your MySQL query statement below

SELECT s1.sale_date, s1.sold_num - s2.sold_num as diff
FROM sales s1 
JOIN sales s2 
ON s1.sale_date = s2.sale_date AND s1.fruit = 'apples' AND s2.fruit = 'oranges'
#ORDER BY sale_date


#SELECT sale_date,
#SUM(
#    CASE
#        WHEN fruit = 'apples' THEN sold_num
#        WHEN fruit = 'oranges' THEN sold_num*-1
#    END
#) as diff
#FROM sales
#GROUP BY sale_date
#ORDER BY sale_date
