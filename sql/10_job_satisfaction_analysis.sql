SELECT
    job_satisfaction,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY job_satisfaction
ORDER BY job_satisfaction;