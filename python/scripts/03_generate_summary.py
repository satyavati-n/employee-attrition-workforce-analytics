import pandas as pd
from pathlib import Path

# Load dataset
df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Overall analysis
total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()
employees_stayed = (df["Attrition"] == "No").sum()
attrition_rate = employees_left / total_employees * 100

# Function to calculate group attrition rates
def get_attrition_summary(column):
    summary = df.groupby(column).agg(
        Total_Employees=("Attrition", "count"),
        Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
    )

    summary["Attrition_Rate"] = (
        summary["Employees_Left"] /
        summary["Total_Employees"] * 100
    )

    return summary.sort_values(
        "Attrition_Rate", ascending=False
    )

# Calculate group analyses
department = get_attrition_summary("Department")
job_role = get_attrition_summary("JobRole")
overtime = get_attrition_summary("OverTime")
marital = get_attrition_summary("MaritalStatus")

# Generate report
report = f"""
EMPLOYEE ATTRITION & WORKFORCE ANALYTICS
PYTHON ANALYSIS SUMMARY
========================================

OVERALL WORKFORCE

Total Employees: {total_employees}
Employees Who Left: {employees_left}
Employees Who Stayed: {employees_stayed}
Overall Attrition Rate: {attrition_rate:.2f}%

AVERAGE METRICS

Average Age: {df["Age"].mean():.2f}
Average Monthly Income: {df["MonthlyIncome"].mean():.2f}

DEPARTMENT FINDINGS

{department.to_string()}

JOB ROLE FINDINGS

{job_role.to_string()}

OVERTIME FINDINGS

{overtime.to_string()}

MARITAL STATUS FINDINGS

{marital.to_string()}


END OF REPORT
"""

# Save report
output_path = Path("python/outputs/python_analysis_summary.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)

output_path.write_text(report, encoding="utf-8")

print(report)
print("Python analysis summary saved successfully!")


import pandas as pd
from pathlib import Path

# 1. LOAD DATASET

df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

output_folder = Path("python/outputs")
output_folder.mkdir(parents=True, exist_ok=True)

print("Dataset loaded successfully!")

# 2. OVERALL WORKFORCE ANALYSIS

total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()
employees_stayed = (df["Attrition"] == "No").sum()

attrition_rate = employees_left / total_employees * 100

overall_summary = pd.DataFrame({
    "Metric": [
        "Total Employees",
        "Employees Left",
        "Employees Stayed",
        "Attrition Rate (%)",
        "Average Age",
        "Average Monthly Income"
    ],
    "Value": [
        total_employees,
        employees_left,
        employees_stayed,
        round(attrition_rate, 2),
        round(df["Age"].mean(), 2),
        round(df["MonthlyIncome"].mean(), 2)
    ]
})

overall_summary.to_csv(
    output_folder / "overall_workforce_summary.csv",
    index=False
)

# 3. GROUP-WISE ATTRITION ANALYSIS

def get_attrition_summary(column):

    summary = df.groupby(column).agg(
        Total_Employees=("Attrition", "count"),
        Employees_Left=(
            "Attrition",
            lambda x: (x == "Yes").sum()
        )
    )

    summary["Employees_Stayed"] = (
        summary["Total_Employees"] -
        summary["Employees_Left"]
    )

    summary["Attrition_Rate"] = (
        summary["Employees_Left"] /
        summary["Total_Employees"] * 100
    )

    return summary.sort_values(
        "Attrition_Rate",
        ascending=False
    ).round(2)


analyses = {
    "department": "Department",
    "job_role": "JobRole",
    "overtime": "OverTime",
    "job_satisfaction": "JobSatisfaction",
    "business_travel": "BusinessTravel",
    "marital_status": "MaritalStatus",
    "job_level": "JobLevel",
    "education_field": "EducationField",
    "distance_from_home": "DistanceFromHome",
    "years_at_company": "YearsAtCompany",
    "years_with_manager": "YearsWithCurrManager"
}

for file_name, column in analyses.items():

    result = get_attrition_summary(column)

    result.to_csv(
        output_folder / f"{file_name}_summary.csv"
    )

    print(f"{column} analysis exported successfully!")

# 4. MONTHLY INCOME ANALYSIS

income_summary = df.groupby("Attrition")["MonthlyIncome"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2)

income_summary.to_csv(
    output_folder / "monthly_income_summary.csv"
)

# 5. AGE GROUP ANALYSIS

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 22, 27, 32, 37, 42, 47, 52, 57, 62],
    labels=[
        "18-22", "23-27", "28-32", "33-37",
        "38-42", "43-47", "48-52", "53-57", "58-62"
    ]
)

age_summary = get_attrition_summary("AgeGroup")

age_summary.to_csv(
    output_folder / "age_group_summary.csv"
)

# 6. DATA QUALITY CHECK

data_quality = pd.DataFrame({
    "Check": [
        "Total Rows",
        "Total Columns",
        "Missing Values",
        "Duplicate Rows",
        "Duplicate Employee Numbers"
    ],
    "Result": [
        df.shape[0],
        df.drop(columns=["AgeGroup"]).shape[1],
        df.isnull().sum().sum(),
        df.duplicated().sum(),
        df["EmployeeNumber"].duplicated().sum()
    ]
})

data_quality.to_csv(
    output_folder / "data_quality_summary.csv",
    index=False
)

# 7. GENERATE TEXT REPORT

report = f"""
EMPLOYEE ATTRITION & WORKFORCE ANALYTICS
PYTHON ANALYSIS REPORT

OVERALL WORKFORCE

Total Employees: {total_employees}
Employees Who Left: {employees_left}
Employees Who Stayed: {employees_stayed}
Overall Attrition Rate: {attrition_rate:.2f}%

AVERAGE METRICS

Average Age: {df["Age"].mean():.2f}
Average Monthly Income: {df["MonthlyIncome"].mean():.2f}

DEPARTMENT ANALYSIS

{get_attrition_summary("Department").to_string()}

JOB ROLE ANALYSIS

{get_attrition_summary("JobRole").to_string()}

OVERTIME ANALYSIS

{get_attrition_summary("OverTime").to_string()}

JOB SATISFACTION ANALYSIS

{get_attrition_summary("JobSatisfaction").to_string()}

BUSINESS TRAVEL ANALYSIS

{get_attrition_summary("BusinessTravel").to_string()}

MARITAL STATUS ANALYSIS

{get_attrition_summary("MaritalStatus").to_string()}

AGE GROUP ANALYSIS

{age_summary.to_string()}

DATA QUALITY

{data_quality.to_string(index=False)}

END OF REPORT
"""

report_path = output_folder / "python_analysis_summary.txt"

report_path.write_text(
    report,
    encoding="utf-8"
)

print("\n" + report)
print("\nAll Python analysis reports exported successfully!")
