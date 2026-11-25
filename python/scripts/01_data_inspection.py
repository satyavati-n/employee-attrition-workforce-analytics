
# Employee Attrition & Workforce Analytics
# Step 1: Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset

df = pd.read_csv("../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")
# Step 3: Display the first five records

print("FIRST FIVE RECORDS")
print(df.head())


# Step 4: Check dataset dimensions

print("\nDATASET SHAPE")
print(df.shape)

# Step 5: Check column names

print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Step 6: Check data types and non-null counts

print("\nDATASET INFORMATION")
df.info()


# Step 7: Check missing values

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nTOTAL MISSING VALUES")
print(df.isnull().sum().sum())

# Step 8: Check duplicate records

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Step 9: Check duplicate employee IDs

print("\nDUPLICATE EMPLOYEE NUMBERS")
print(df["EmployeeNumber"].duplicated().sum())


# Step 10: Basic statistical analysis

print("\nBASIC HR STATISTICS")

# Total employees
total_employees = len(df)

# Employees who left
employees_left = (df["Attrition"] == "Yes").sum()

# Employees who stayed
employees_stayed = (df["Attrition"] == "No").sum()

# Overall attrition rate
attrition_rate = np.round(
    (employees_left / total_employees) * 100, 2
)

# Average employee age
average_age = np.round(df["Age"].mean(), 2)

# Average monthly income
average_income = np.round(df["MonthlyIncome"].mean(), 2)

print("Total Employees:", total_employees)
print("Employees Left:", employees_left)
print("Employees Stayed:", employees_stayed)
print("Attrition Rate:", attrition_rate, "%")
print("Average Age:", average_age)
print("Average Monthly Income:", average_income)


# Step 11: Department-wise attrition analysis

print("\nDEPARTMENT-WISE ATTRITION")

department_analysis = df.groupby("Department").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

department_analysis["Attrition_Rate"] = (
    department_analysis["Employees_Left"] /
    department_analysis["Total_Employees"] * 100
).round(2)

print(department_analysis)



# Step 12: Export department analysis

department_analysis.to_csv(
    "outputs/department_attrition_analysis.csv"
)

print("\nDepartment analysis exported successfully!")

# Step 13: Job Role-wise attrition analysis

jobrole_analysis = df.groupby("JobRole").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

jobrole_analysis["Attrition_Rate"] = (
    jobrole_analysis["Employees_Left"] /
    jobrole_analysis["Total_Employees"] * 100
).round(2)

print("\nJOB ROLE-WISE ATTRITION")
print(jobrole_analysis)

# Export job role analysis
jobrole_analysis.to_csv(
    "outputs/job_role_attrition_analysis.csv"
)

print("\nJob role analysis exported successfully!")

# Step 14: Overtime-wise attrition analysis

overtime_analysis = df.groupby("OverTime").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

overtime_analysis["Attrition_Rate"] = (
    overtime_analysis["Employees_Left"] /
    overtime_analysis["Total_Employees"] * 100
).round(2)

print("\nOVERTIME-WISE ATTRITION")
print(overtime_analysis)

# Export overtime analysis
overtime_analysis.to_csv(
    "outputs/overtime_attrition_analysis.csv"
)

print("\nOvertime analysis exported successfully!")

# Step 15: Job Satisfaction-wise attrition analysis

satisfaction_analysis = df.groupby("JobSatisfaction").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

satisfaction_analysis["Attrition_Rate"] = (
    satisfaction_analysis["Employees_Left"] /
    satisfaction_analysis["Total_Employees"] * 100
).round(2)

print("\nJOB SATISFACTION-WISE ATTRITION")
print(satisfaction_analysis)

# Export satisfaction analysis
satisfaction_analysis.to_csv(
    "outputs/job_satisfaction_attrition_analysis.csv"
)

print("\nJob satisfaction analysis exported successfully!")

# Step 16: Monthly Income vs Attrition

income_analysis = df.groupby("Attrition").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean")
)

income_analysis["Average_Monthly_Income"] = (
    income_analysis["Average_Monthly_Income"].round(2)
)

print("\nMONTHLY INCOME VS ATTRITION")
print(income_analysis)

# Export income analysis
income_analysis.to_csv(
    "outputs/monthly_income_attrition_analysis.csv"
)

print("\nMonthly income analysis exported successfully!")

# Step 17: Years at Company vs Attrition

experience_analysis = df.groupby("YearsAtCompany").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

experience_analysis["Attrition_Rate"] = (
    experience_analysis["Employees_Left"] /
    experience_analysis["Total_Employees"] * 100
).round(2)

print("\nYEARS AT COMPANY VS ATTRITION")
print(experience_analysis)

# Export experience analysis
experience_analysis.to_csv(
    "outputs/years_at_company_attrition_analysis.csv"
)

print("\nYears at company analysis exported successfully!")

# Step 18: Age Group vs Attrition

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 22, 27, 32, 37, 42, 47, 52, 57, 62],
    labels=[
        "18-22", "23-27", "28-32", "33-37",
        "38-42", "43-47", "48-52", "53-57", "58-62"
    ]
)

age_analysis = df.groupby("Age_Group", observed=False).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

age_analysis["Attrition_Rate"] = (
    age_analysis["Employees_Left"] /
    age_analysis["Total_Employees"] * 100
).round(2)

print("\nAGE GROUP-WISE ATTRITION")
print(age_analysis)

# Export age analysis
age_analysis.to_csv(
    "outputs/age_group_attrition_analysis.csv"
)

print("\nAge group analysis exported successfully!")

# Step 19: Business Travel vs Attrition

travel_analysis = df.groupby("BusinessTravel").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

travel_analysis["Attrition_Rate"] = (
    travel_analysis["Employees_Left"] /
    travel_analysis["Total_Employees"] * 100
).round(2)

print("\nBUSINESS TRAVEL VS ATTRITION")
print(travel_analysis)

# Export travel analysis
travel_analysis.to_csv(
    "outputs/business_travel_attrition_analysis.csv"
)

print("\nBusiness travel analysis exported successfully!")

# Step 20: Marital Status vs Attrition

marital_analysis = df.groupby("MaritalStatus").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

marital_analysis["Attrition_Rate"] = (
    marital_analysis["Employees_Left"] /
    marital_analysis["Total_Employees"] * 100
).round(2)

print("\nMARITAL STATUS VS ATTRITION")
print(marital_analysis)

# Export marital status analysis
marital_analysis.to_csv(
    "outputs/marital_status_attrition_analysis.csv"
)

print("\nMarital status analysis exported successfully!")

# Step 21: Job Level vs Attrition

joblevel_analysis = df.groupby("JobLevel").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

joblevel_analysis["Attrition_Rate"] = (
    joblevel_analysis["Employees_Left"] /
    joblevel_analysis["Total_Employees"] * 100
).round(2)

print("\nJOB LEVEL VS ATTRITION")
print(joblevel_analysis)

# Export job level analysis
joblevel_analysis.to_csv(
    "outputs/job_level_attrition_analysis.csv"
)

print("\nJob level analysis exported successfully!")

# Step 22: Distance From Home vs Attrition

df["Distance_Group"] = pd.cut(
    df["DistanceFromHome"],
    bins=[0, 5, 10, 15, 20, 25, 30],
    labels=["1-5", "6-10", "11-15", "16-20", "21-25", "26-30"]
)

distance_analysis = df.groupby("Distance_Group", observed=False).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

distance_analysis["Attrition_Rate"] = (
    distance_analysis["Employees_Left"] /
    distance_analysis["Total_Employees"] * 100
).round(2)

print("\nDISTANCE FROM HOME VS ATTRITION")
print(distance_analysis)

# Export distance analysis
distance_analysis.to_csv(
    "outputs/distance_from_home_attrition_analysis.csv"
)

print("\nDistance analysis exported successfully!")

# Step 23: Years With Current Manager vs Attrition

manager_analysis = df.groupby("YearsWithCurrManager").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

manager_analysis["Attrition_Rate"] = (
    manager_analysis["Employees_Left"] /
    manager_analysis["Total_Employees"] * 100
).round(2)

print("\nYEARS WITH CURRENT MANAGER VS ATTRITION")
print(manager_analysis)

# Export manager analysis
manager_analysis.to_csv(
    "outputs/years_with_manager_attrition_analysis.csv"
)

print("\nManager analysis exported successfully!")

# Step 24: Education Field vs Attrition

education_analysis = df.groupby("EducationField").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

education_analysis["Attrition_Rate"] = (
    education_analysis["Employees_Left"] /
    education_analysis["Total_Employees"] * 100
).round(2)

print("\nEDUCATION FIELD VS ATTRITION")
print(education_analysis)

# Export education analysis
education_analysis.to_csv(
    "outputs/education_field_attrition_analysis.csv"
)

print("\nEducation field analysis exported successfully!")