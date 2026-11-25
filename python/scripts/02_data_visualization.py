
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Step 2: Calculate department-wise attrition
department_analysis = df.groupby("Department").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

department_analysis["Attrition_Rate"] = (
    department_analysis["Employees_Left"] /
    department_analysis["Total_Employees"] * 100
).round(2)

# Step 3: Create bar chart
plt.figure(figsize=(10, 6))

sns.barplot(
    data=department_analysis.reset_index(),
    x="Department",
    y="Attrition_Rate"
)

# Step 4: Add chart title and labels
plt.title("Department-wise Employee Attrition Rate", fontsize=15)
plt.xlabel("Department", fontsize=12)
plt.ylabel("Attrition Rate (%)", fontsize=12)

# Step 5: Display percentage values
for index, value in enumerate(department_analysis["Attrition_Rate"]):
    plt.text(index, value + 0.3, f"{value:.2f}%", ha="center")

plt.tight_layout()

# Step 6: Save chart
plt.savefig(
    "python/charts/department_attrition_rate.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Department attrition chart saved successfully!")



# Step 7: Job Role-wise Attrition Analysis

jobrole_analysis = df.groupby("JobRole").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

jobrole_analysis["Attrition_Rate"] = (
    jobrole_analysis["Employees_Left"] /
    jobrole_analysis["Total_Employees"] * 100
).round(2)

# Sort job roles by attrition rate
jobrole_plot = jobrole_analysis.reset_index().sort_values(
    by="Attrition_Rate"
)

# Create horizontal bar chart
plt.figure(figsize=(11, 7))

ax = sns.barplot(
    data=jobrole_plot,
    x="Attrition_Rate",
    y="JobRole"
)

plt.title("Job Role-wise Employee Attrition Rate", fontsize=15)
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Job Role")

# Add percentage labels
for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%", padding=4)

plt.tight_layout()

# Save chart
plt.savefig(
    "python/charts/job_role_attrition_rate.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Job role attrition chart saved successfully!")



# Step 8: Overtime vs Attrition

overtime_analysis = df.groupby("OverTime").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

overtime_analysis["Attrition_Rate"] = (
    overtime_analysis["Employees_Left"] /
    overtime_analysis["Total_Employees"] * 100
).round(2)

# Create bar chart
plt.figure(figsize=(8, 5))

ax = sns.barplot(
    data=overtime_analysis.reset_index(),
    x="OverTime",
    y="Attrition_Rate"
)

plt.title("Overtime vs Employee Attrition Rate", fontsize=15)
plt.xlabel("Works Overtime")
plt.ylabel("Attrition Rate (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%", padding=4)

plt.tight_layout()

# Save chart
plt.savefig(
    "python/charts/overtime_attrition_rate.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Overtime attrition chart saved successfully!")



# Step 9: Job Satisfaction vs Attrition

satisfaction_analysis = df.groupby("JobSatisfaction").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

satisfaction_analysis["Attrition_Rate"] = (
    satisfaction_analysis["Employees_Left"] /
    satisfaction_analysis["Total_Employees"] * 100
).round(2)

# Create bar chart
plt.figure(figsize=(9, 5))

ax = sns.barplot(
    data=satisfaction_analysis.reset_index(),
    x="JobSatisfaction",
    y="Attrition_Rate"
)

plt.title("Job Satisfaction vs Employee Attrition Rate", fontsize=15)
plt.xlabel("Job Satisfaction Level (1 = Low, 4 = Very High)")
plt.ylabel("Attrition Rate (%)")

for container in ax.containers:
    ax.bar_label(container, fmt="%.2f%%", padding=4)

plt.tight_layout()

# Save chart
plt.savefig(
    "python/charts/job_satisfaction_attrition_rate.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Job satisfaction chart saved successfully!")



# Step 10: Monthly Income vs Attrition

plt.figure(figsize=(9, 6))

sns.boxplot(
    data=df,
    x="Attrition",
    y="MonthlyIncome"
)

plt.title("Monthly Income Distribution by Attrition", fontsize=15)
plt.xlabel("Employee Attrition")
plt.ylabel("Monthly Income")

plt.tight_layout()

# Save chart
plt.savefig(
    "python/charts/monthly_income_attrition.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Monthly income chart saved successfully!")


# Step 11: Years at Company vs Attrition

experience_analysis = df.groupby("YearsAtCompany").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

experience_analysis["Attrition_Rate"] = (
    experience_analysis["Employees_Left"] /
    experience_analysis["Total_Employees"] * 100
).round(2)

# Create line chart
plt.figure(figsize=(11, 6))

sns.lineplot(
    data=experience_analysis.reset_index(),
    x="YearsAtCompany",
    y="Attrition_Rate",
    marker="o"
)

plt.title("Years at Company vs Employee Attrition Rate", fontsize=15)
plt.xlabel("Years at Company")
plt.ylabel("Attrition Rate (%)")
plt.xticks(range(0, int(df["YearsAtCompany"].max()) + 1, 2))
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save chart
plt.savefig(
    "python/charts/years_at_company_attrition.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Years at company chart saved successfully!")

# 7. Age Group vs Attrition Rate

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 22, 27, 32, 37, 42, 47, 52, 57, 62],
    labels=["18-22", "23-27", "28-32", "33-37",
            "38-42", "43-47", "48-52", "53-57", "58-62"]
)

age_attrition = df.groupby("AgeGroup", observed=False).agg(
    Total_Employees=("Attrition", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

age_attrition["Attrition_Rate"] = (
    age_attrition["Employees_Left"] /
    age_attrition["Total_Employees"] * 100
)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=age_attrition.index,
    y=age_attrition["Attrition_Rate"]
)

plt.title("Age Group vs Attrition Rate")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("python/charts/age_group_attrition_rate.png")
plt.show()

print("Age group attrition chart saved successfully!")


# 8. Business Travel vs Attrition Rate

travel_attrition = df.groupby("BusinessTravel").agg(
    Total_Employees=("Attrition", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

travel_attrition["Attrition_Rate"] = (
    travel_attrition["Employees_Left"] /
    travel_attrition["Total_Employees"] * 100
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=travel_attrition.index,
    y=travel_attrition["Attrition_Rate"]
)

plt.title("Business Travel vs Attrition Rate")
plt.xlabel("Business Travel")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig("python/charts/business_travel_attrition_rate.png")
plt.show()

print("Business travel attrition chart saved successfully!")

# 9. Marital Status vs Attrition Rate

marital_attrition = df.groupby("MaritalStatus").agg(
    Total_Employees=("Attrition", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

marital_attrition["Attrition_Rate"] = (
    marital_attrition["Employees_Left"] /
    marital_attrition["Total_Employees"] * 100
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=marital_attrition.index,
    y=marital_attrition["Attrition_Rate"]
)

plt.title("Marital Status vs Attrition Rate")
plt.xlabel("Marital Status")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig("python/charts/marital_status_attrition_rate.png")
plt.show()

print("Marital status attrition chart saved successfully!")

# 10. Job Level vs Attrition Rate

job_level_attrition = df.groupby("JobLevel").agg(
    Total_Employees=("Attrition", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

job_level_attrition["Attrition_Rate"] = (
    job_level_attrition["Employees_Left"] /
    job_level_attrition["Total_Employees"] * 100
)

plt.figure(figsize=(8, 5))
sns.barplot(x=job_level_attrition.index,
            y=job_level_attrition["Attrition_Rate"])

plt.title("Job Level vs Attrition Rate")
plt.xlabel("Job Level")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig("python/charts/job_level_attrition_rate.png")
plt.show()

print("Job level chart saved successfully!")

# 11. Distance From Home vs Attrition Rate

df["DistanceGroup"] = pd.cut(
    df["DistanceFromHome"],
    bins=[0, 5, 10, 15, 20, 25, 30],
    labels=["1-5", "6-10", "11-15", "16-20", "21-25", "26-30"]
)

distance_attrition = df.groupby("DistanceGroup", observed=False).agg(
    Total_Employees=("Attrition", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

distance_attrition["Attrition_Rate"] = (
    distance_attrition["Employees_Left"] /
    distance_attrition["Total_Employees"] * 100
)

plt.figure(figsize=(9, 5))
sns.barplot(x=distance_attrition.index,
            y=distance_attrition["Attrition_Rate"])

plt.title("Distance From Home vs Attrition Rate")
plt.xlabel("Distance From Home")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig("python/charts/distance_from_home_attrition_rate.png")
plt.show()

print("Distance from home chart saved successfully!")

# 12. Years With Current Manager vs Attrition Rate

manager_attrition = df.groupby("YearsWithCurrManager").agg(
    Total_Employees=("Attrition", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

manager_attrition["Attrition_Rate"] = (
    manager_attrition["Employees_Left"] /
    manager_attrition["Total_Employees"] * 100
)

plt.figure(figsize=(10, 5))
sns.lineplot(
    x=manager_attrition.index,
    y=manager_attrition["Attrition_Rate"],
    marker="o"
)

plt.title("Years With Current Manager vs Attrition Rate")
plt.xlabel("Years With Current Manager")
plt.ylabel("Attrition Rate (%)")
plt.grid(True)
plt.tight_layout()

plt.savefig("python/charts/years_with_manager_attrition_rate.png")
plt.show()

print("Years with current manager chart saved successfully!")

# 13. Education Field vs Attrition Rate

education_attrition = df.groupby("EducationField").agg(
    Total_Employees=("Attrition", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

education_attrition["Attrition_Rate"] = (
    education_attrition["Employees_Left"] /
    education_attrition["Total_Employees"] * 100
)

education_attrition = education_attrition.sort_values(
    "Attrition_Rate", ascending=False
)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=education_attrition["Attrition_Rate"],
    y=education_attrition.index
)

plt.title("Education Field vs Attrition Rate")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Education Field")
plt.tight_layout()

plt.savefig("python/charts/education_field_attrition_rate.png")
plt.show()

print("Education field chart saved successfully!")