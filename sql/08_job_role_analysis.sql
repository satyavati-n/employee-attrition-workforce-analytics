SELECT
    job_role,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    COUNT(*) FILTER (WHERE attrition = 'No') AS employees_stayed,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY job_role
ORDER BY attrition_rate DESC;