SELECT
    CASE
        WHEN age BETWEEN 18 AND 22 THEN '18-22'
        WHEN age BETWEEN 23 AND 27 THEN '23-27'
        WHEN age BETWEEN 28 AND 32 THEN '28-32'
        WHEN age BETWEEN 33 AND 37 THEN '33-37'
        WHEN age BETWEEN 38 AND 42 THEN '38-42'
        WHEN age BETWEEN 43 AND 47 THEN '43-47'
        WHEN age BETWEEN 48 AND 52 THEN '48-52'
        WHEN age BETWEEN 53 AND 57 THEN '53-57'
        WHEN age BETWEEN 58 AND 62 THEN '58-62'
    END AS age_group,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY age_group
ORDER BY MIN(age);