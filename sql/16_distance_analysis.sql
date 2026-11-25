SELECT
    CASE
        WHEN distance_from_home BETWEEN 1 AND 5 THEN '1-5'
        WHEN distance_from_home BETWEEN 6 AND 10 THEN '6-10'
        WHEN distance_from_home BETWEEN 11 AND 15 THEN '11-15'
        WHEN distance_from_home BETWEEN 16 AND 20 THEN '16-20'
        WHEN distance_from_home BETWEEN 21 AND 25 THEN '21-25'
        WHEN distance_from_home BETWEEN 26 AND 30 THEN '26-30'
    END AS distance_group,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY distance_group
ORDER BY MIN(distance_from_home);