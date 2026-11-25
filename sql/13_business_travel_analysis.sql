SELECT
    business_travel,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY business_travel
ORDER BY attrition_rate DESC;