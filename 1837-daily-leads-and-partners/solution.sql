# Write your MySQL query statement below
SELECT
date_id, make_name,
COUNT(DISTINCT partner_id) as unique_partners,
COUNT(DISTINCT lead_id) as unique_leads
FROM dailysales
GROUP BY date_id, make_name

