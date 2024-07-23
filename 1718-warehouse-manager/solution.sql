# Write your MySQL query statement below
 

    SELECT name as warehouse_name, SUM(width*length*height*units) as volume
    FROM products p
    JOIN warehouse w ON p.product_id = w.product_id
    GROUP BY name

#SELECT name as warehouse_name, SUM(v_per_unit*units) as volume FROM T 

