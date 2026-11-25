**Employee Attrition & Workforce Analytics**

**Project Overview**

This project analyzes employee attrition and workforce data to identify patterns and factors associated with employees leaving an organization.

The objective is to explore workforce trends, understand employee attrition across different categories, and generate meaningful business insights that can support HR decision-making.

 **Business Objectives**

- Calculate the overall employee attrition rate.
- Analyze attrition across departments and job roles.
- Understand the relationship between overtime and employee attrition.
- Examine attrition based on age, income, job satisfaction and years at the company.
- Identify workforce patterns and potential areas of concern for HR teams.

 **Tools & Technologies**

- **Microsoft Excel:** Data exploration, PivotTables and analysis.
- **Python:** Data inspection, data analysis and visualization.
- **Pandas:** Data manipulation and analysis.
- **NumPy:** Numerical operations.
- **Matplotlib & Seaborn:** Data visualization.
- **PostgreSQL:** Analyze employee data, identify key factors influencing employee attrition and workforce trends.

**Project Structure**

```text
employee-attrition-workforce-analytics/
│
├── data/
│   └── raw/
│       └── HR Employee Attrition Dataset.csv
│
├── excel/
│   └── HR_Attrition_Analysis.xlsx
│
├── python/
│   ├── charts/
│   ├── outputs/
│   └── scripts/
│       ├── 01_data_inspection.py
│       ├── 02_data_visualization.py
│       └── 03_generate_summary.py
│
├── screenshots/
│
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_table.sql
│   └── ... (additional analysis queries)
│
└── README.md
```

**Dataset Information**

- **Dataset:** IBM HR Analytics Employee Attrition & Performance
- **Total Records:** 1,470 employees
- **Total Columns:** 35
- **Target Variable:** Attrition
- **Attrition Categories:** Yes and No

**Analysis Performed**

**1. Excel Analysis**

Created PivotTable-based analyses covering:

- Department-wise attrition
- Job role-wise attrition
- Overtime and attrition
- Job satisfaction and attrition
- Monthly income and attrition
- Years at company and attrition
- Age group and attrition
- Business travel and attrition
- Marital status and attrition
- Job level and attrition
- Distance from home and attrition
- Years with current manager and attrition
- Education field and attrition

**2. Python Analysis**

Used Python libraries to:

- Inspect dataset structure and data quality.
- Analyze employee attrition patterns.
- Calculate summary statistics.
- Generate visualizations for different workforce factors.
- Export analysis results into CSV files.

**3. PostgreSQL SQL Query Development**

Prepared SQL queries covered business-focused workforce analysis, including:

- Database and table creation.
- Data exploration and quality checks.
- Overall attrition analysis.
- Department and job role analysis.
- Overtime and job satisfaction analysis.
- Income, age and experience analysis.
- Additional workforce insights.

**Key Findings**

- **Overall Attrition Rate:** 16.12%
- **Employees Who Left:** 237
- **Employees Who Stayed:** 1,233
- **Highest Department Attrition Rate:** Sales (20.63%)
- **Overtime Attrition Rate:** 30.53%
- **Average Monthly Income of Employees Who Left:** 4,787.09
- **Average Monthly Income of Employees Who Stayed:** 6,832.74

**Business Insights**

- Employees working overtime showed a higher attrition rate than employees not working overtime.
- The Sales department had the highest attrition rate among the three departments.
- Employees with lower job satisfaction levels generally showed higher attrition rates.
- Employees who left had a lower average monthly income than employees who stayed.
- Attrition patterns varied across age groups and job roles.

**Project Screenshots**

The `screenshots` folder contains selected Excel and Python analysis visuals to demonstrate the work completed in this project.

**Skills Demonstrated**

- Data cleaning and inspection
- Exploratory Data Analysis (EDA)
- Excel PivotTables
- Python data analysis
- Data visualization
- SQL query development
- Business problem-solving
- HR analytics

**Conclusion**

This project demonstrates how Excel, Python and SQL can be used to explore employee attrition and workforce trends.

The analysis highlights patterns that HR teams can investigate further to better understand employee retention and workforce challenges.

---

**Project Type:** Data Analytics | HR Analytics

**Tools Used:** Excel | Python | PostgreSQL
