\# Employee Attrition \& Workforce Analysis



\## Project Overview



Employee attrition is a major challenge for organizations because losing employees can increase recruitment costs, affect productivity, and create workforce management difficulties.



This project analyzes employee data to identify patterns and factors associated with employee attrition. It explores how employee characteristics, job roles, departments, satisfaction levels, income, overtime, and other factors relate to employees leaving the organization.



The project uses \*\*Microsoft Excel, Python, and PostgreSQL\*\* to organize and analyze the HR dataset.



\## Business Objectives



\- Calculate the overall employee attrition rate.

\- Identify departments and job roles with higher attrition.

\- Analyze the relationship between overtime and employee attrition.

\- Explore how job satisfaction and monthly income relate to attrition.

\- Analyze attrition across different age groups and experience levels.

\- Generate insights that can support HR workforce planning and employee retention strategies.



\## Tools \& Technologies



| Tool | Purpose |

|---|---|

| Microsoft Excel | Data exploration and PivotTable analysis |

| Python | Data analysis, data visualization, and summary generation |

| PostgreSQL | Database design and SQL query development |

| Pandas | Data manipulation and analysis |

| NumPy | Numerical operations |

| Matplotlib | Data visualization |

| Seaborn | Statistical data visualization |



\## Dataset Information



\- \*\*Dataset:\*\* IBM HR Analytics Employee Attrition \& Performance

\- \*\*Total Records:\*\* 1,470 employees

\- \*\*Total Columns:\*\* 35

\- \*\*Domain:\*\* Human Resources



The dataset contains employee information such as age, department, job role, monthly income, job satisfaction, overtime, years at company, and attrition status.



\## Project Workflow



\### 1. Excel Analysis



Used Microsoft Excel to explore the HR dataset and create PivotTable analyses.



Key analysis areas:

\- Department vs Attrition

\- Job Role vs Attrition

\- Overtime vs Attrition

\- Job Satisfaction vs Attrition

\- Monthly Income vs Attrition

\- Age Group vs Attrition

\- Years at Company vs Attrition

\- Business Travel vs Attrition

\- Marital Status vs Attrition

\- Job Level vs Attrition

\- Distance From Home vs Attrition

\- Years With Current Manager vs Attrition

\- Education Field vs Attrition



\### 2. Python Analysis



Used Python libraries to inspect the dataset, perform analysis, generate summary outputs, and create visualizations.



Libraries used:

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn



Python analysis included:

\- Dataset inspection

\- Attrition distribution analysis

\- Department-wise analysis

\- Age-group analysis

\- Job-role analysis

\- Summary generation

\- CSV exports and visualizations



\### 3. PostgreSQL Analysis



Developed SQL scripts for HR business questions using PostgreSQL.



The SQL scripts cover database setup, table creation, and employee attrition analysis queries.



\## Key Findings



Based on the dataset analysis:



\- \*\*Overall Attrition Rate:\*\* 16.12%

\- \*\*Employees Who Left:\*\* 237

\- \*\*Employees Who Stayed:\*\* 1,233

\- \*\*Total Employees:\*\* 1,470



\### Department-wise Attrition



| Department | Attrition Rate |

|---|---:|

| Human Resources | 19.05% |

| Research \& Development | 13.84% |

| Sales | 20.63% |



\### Overtime Analysis



| Overtime | Attrition Rate |

|---|---:|

| No | 10.44% |

| Yes | 30.53% |



Employees working overtime had a higher attrition rate in this dataset.



\### Monthly Income Analysis



| Attrition Status | Average Monthly Income |

|---|---:|

| Stayed | 6,832.74 |

| Left | 4,787.09 |



Employees who left had a lower average monthly income than employees who stayed.



\## Business Insights



1\. The Sales department has the highest attrition rate among the three departments.

2\. Employees working overtime show a substantially higher attrition rate.

3\. Employees who left had a lower average monthly income.

4\. Job satisfaction and employee experience are useful dimensions for further HR analysis.



These findings show patterns and associations in the dataset; they do not establish that any single factor causes employees to leave.



\## Project Structure



```text

employee-attrition-workforce-analytics/

│

├── data/

│

├── excel/

│

├── python/

│   ├── scripts/

│   ├── outputs/

│   └── charts/

│

├── sql/

│

├── screenshots/

│

└── README.md

```



\## Conclusion



This project demonstrates how Excel, Python, and PostgreSQL can be used in an HR analytics workflow to explore employee attrition and workforce patterns.



The analysis highlights important areas that HR teams can investigate further to support employee retention and workforce planning.





