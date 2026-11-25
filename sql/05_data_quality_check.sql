-- Total records
SELECT COUNT(*) AS total_records
FROM employees;

-- Check missing values
SELECT
    COUNT(*) FILTER (WHERE age IS NULL) AS missing_age,
    COUNT(*) FILTER (WHERE attrition IS NULL) AS missing_attrition,
    COUNT(*) FILTER (WHERE department IS NULL) AS missing_department,
    COUNT(*) FILTER (WHERE job_role IS NULL) AS missing_job_role,
    COUNT(*) FILTER (WHERE monthly_income IS NULL) AS missing_monthly_income
FROM employees;

-- Check duplicate employee numbers
SELECT
    employee_number,
    COUNT(*) AS duplicate_count
FROM employees
GROUP BY employee_number
HAVING COUNT(*) > 1;

-- Check duplicate records
SELECT COUNT(*) AS duplicate_records
FROM (
    SELECT *
    FROM employees
    GROUP BY
        age, attrition, business_travel, daily_rate,
        department, distance_from_home, education,
        education_field, employee_count, employee_number,
        environment_satisfaction, gender, hourly_rate,
        job_involvement, job_level, job_role,
        job_satisfaction, marital_status, monthly_income,
        monthly_rate, num_companies_worked, over18,
        over_time, percent_salary_hike, performance_rating,
        relationship_satisfaction, standard_hours,
        stock_option_level, total_working_years,
        training_times_last_year, work_life_balance,
        years_at_company, years_in_current_role,
        years_since_last_promotion, years_with_curr_manager
    HAVING COUNT(*) > 1
) AS duplicates;