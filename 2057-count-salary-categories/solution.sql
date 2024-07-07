WITH S AS (
    SELECT account_id, income,
    CASE
        WHEN income < 20000 THEN 'Low Salary'
        WHEN income > 50000 THEN 'High Salary'
        ELSE 'Average Salary'
    END AS category
    FROM accounts
),
W AS (
    SELECT category, COUNT(*) AS accounts_count
    FROM S
    GROUP BY category
),
categories AS (
    SELECT 'Low Salary' as category
    UNION
    SELECT 'Average Salary' as category
    UNION
    SELECT 'High Salary' as category
)
SELECT c.category,
       COALESCE(w.accounts_count, 0) AS accounts_count
FROM categories c
LEFT JOIN W w ON c.category = w.category;

