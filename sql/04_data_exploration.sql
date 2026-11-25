-- View all employee records
SELECT *
FROM employees;

-- View first 10 records
SELECT *
FROM employees
LIMIT 10;

-- Count total employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- View all column values from selected fields
SELECT DISTINCT department
FROM employees;

SELECT DISTINCT job_role
FROM employees;

SELECT DISTINCT attrition
FROM employees;

-- Check the number of unique departments
SELECT COUNT(DISTINCT department) AS total_departments
FROM employees;

-- Check the number of unique job roles
SELECT COUNT(DISTINCT job_role) AS total_job_roles
FROM employees;