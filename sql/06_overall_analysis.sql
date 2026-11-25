-- Total employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Employees who left
SELECT COUNT(*) AS employees_left
FROM employees
WHERE attrition = 'Yes';

-- Employees who stayed
SELECT COUNT(*) AS employees_stayed
FROM employees
WHERE attrition = 'No';

-- Overall attrition rate
SELECT
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    COUNT(*) AS total_employees,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees;

-- Average age and monthly income
SELECT
    ROUND(AVG(age), 2) AS average_age,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income
FROM employees;