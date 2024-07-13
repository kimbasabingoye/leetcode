WITH cumulative_weights AS (
    SELECT
        turn,
        person_name,
        weight,
        SUM(weight) OVER (ORDER BY turn) AS cumul_weight
    FROM
        queue
)
SELECT
    person_name
FROM
    cumulative_weights
WHERE
    cumul_weight <= 1000
ORDER BY
    turn DESC
LIMIT 1;

