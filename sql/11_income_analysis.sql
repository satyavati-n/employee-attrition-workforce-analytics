-- Average monthly income by attrition status
SELECT
    attrition,
    COUNT(*) AS total_employees,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income,
    ROUND(MIN(monthly_income), 2) AS minimum_income,
    ROUND(MAX(monthly_income), 2) AS maximum_income
FROM employees
GROUP BY attrition;

-- Average income by department
SELECT
    department,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income
FROM employees
GROUP BY department
ORDER BY average_monthly_income DESC;

-- Average income by job role
SELECT
    job_role,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income
FROM employees
GROUP BY job_role
ORDER BY average_monthly_income DESC;