-- 1. Department with the highest attrition rate

SELECT
    department,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY department
ORDER BY attrition_rate DESC
LIMIT 1;


-- 2. Job role with the highest attrition rate

SELECT
    job_role,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY job_role
ORDER BY attrition_rate DESC
LIMIT 1;


-- 3. Attrition comparison by overtime

SELECT
    over_time,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY over_time
ORDER BY attrition_rate DESC;


-- 4. Attrition comparison by monthly income

SELECT
    attrition,
    COUNT(*) AS total_employees,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income
FROM employees
GROUP BY attrition;


-- 5. Attrition comparison by job satisfaction

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
ORDER BY attrition_rate DESC;


-- 6. Attrition comparison by years at company

SELECT
    years_at_company,
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS attrition_rate
FROM employees
GROUP BY years_at_company
ORDER BY years_at_company;


-- 7. Overall workforce summary

SELECT
    COUNT(*) AS total_employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    COUNT(*) FILTER (WHERE attrition = 'No') AS employees_stayed,
    ROUND(
        COUNT(*) FILTER (WHERE attrition = 'Yes') * 100.0
        / NULLIF(COUNT(*), 0), 2
    ) AS overall_attrition_rate,
    ROUND(AVG(age), 2) AS average_age,
    ROUND(AVG(monthly_income), 2) AS average_monthly_income
FROM employees;