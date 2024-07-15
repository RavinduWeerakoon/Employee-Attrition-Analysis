Employee Attrition Analysis
===========================

Overview
--------

This project aims to analyze employee attrition at Marvelous Construction, a major construction firm in Sri Lanka. Our analysis seeks to provide valuable insights to help the company's CEO make strategic decisions to improve employee retention.

Table of Contents
-----------------

1.  [Problem Overview](#problem-overview)
2.  [Dataset Description](#dataset-description)
3.  [Data Preprocessing](#data-preprocessing)
4.  [Predictive Analysis](#predictive-analysis)
5.  [Insights from Data Analysis](#insights-from-data-analysis)
6.  [Hypothesis Testing Results](#hypothesis-testing-results)
7.  [Conclusions and Recommendations](#conclusions-and-recommendations)
8.  [How to Run the Code](#how-to-run-the-code)

Problem Overview
----------------

Marvelous Construction has noticed a high rate of employee resignations. We analyzed a dataset containing employee details, attendance, leaves, and salary information to address this issue. Our goal was to derive insights to help reduce employee attrition.

Dataset Description
-------------------

-   **Data Source**: Human Resources department of Marvelous Construction.
-   **Data Collection Method**: Collected through the company's ERP system.
-   **Data Format**: CSV (Comma-Separated Values) files.
-   **Data Size**:
    -   Employee Dataset: 631 records, 17 attributes
    -   Leaves Dataset: 237 records, 6 attributes
    -   Salary Dataset: 2632 records, 4 attributes
    -   Attendance Dataset: 60354 records, 10 attributes
-   **Data Quality Issues**: Missing values, redundant attributes, unknown attributes, categorical variables, outliers.

Data Preprocessing
------------------

1.  **Data Integration**: Merged necessary features from the four CSV files into a single dataset named "marvelous".
2.  **Remove Redundant Attributes**: Removed attributes like "Religion" and "Designation".
3.  **Remove Irrelevant Attributes**: Removed attributes such as "Employee_No", "Employee_Code", "Name", "Title".
4.  **Categorical Columns Encoding**: Applied binary, ordinal, and one-hot encoding techniques.
5.  **Impute Missing Values**: Used KNN imputer to handle missing values in "Year_of_Birth" and "Net Salary".
6.  **Data Transformation**: Applied Min-Max Scalar to 'Year_of_Birth', 'ages_in_the_company', and 'Net Salary' columns.

Predictive Analysis
-------------------

We employed an XGBoost classification model to assess the quality of our data preprocessing steps. The model achieved an accuracy of 0.89, indicating a strong ability to learn from the prepared data.

Insights from Data Analysis
---------------------------

-   The workforce is relatively young.
-   Married employees tend to be older than unmarried ones.
-   Management employees are older compared to other categories.
-   A higher proportion of contract-based workers are inactive.
-   A larger proportion of males are married compared to females.

Hypothesis Testing Results
--------------------------

1.  **Employment Category Impact**: Statistically significant impact on employment status.
2.  **Employment Type Impact**: Statistically significant impact on employment status.
3.  **Gender and Salary**: No significant difference in salary between genders.
4.  **Net Salary Impact**: The statistically significant relationship between salary and employment status.
5.  **Religion Impact**: No significant impact on employment status.

Conclusions and Recommendations
-------------------------------

To minimize employee resignations, we recommend:

1.  Hiring more permanent employees.
2.  Increasing employee salaries.
3.  Providing incentives to retain employees in the "Labour" category.

How to Run the Code
-------------------

1.  Clone the repository:

    bash

    Copy code

    `git clone https://github.com/RavinduWeerakoon/Employee-Attrition-Analysis.git
    cd Employee-Attrition-Analysis`

2.  Install the required packages:

    bash

    Copy code

    `pip install -r requirements.txt`

3.  Run the analysis:

    bash

    Copy code

    `python 18.py`

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Contact
-------

For any inquiries, please get in touch with the project members:

-[Ravindu Weerakoon](ravindu.21@cse.mrt.ac.lk)
-[Lakindu Kariyawasam](lakindu.21@cse.mrt.ac.lk)
-[Eshan Madurange](eshan.21@cse.mrt.ac.lk)
-[Nethum Rathnayake(nethum.21@cse.mrt.ac.lk)
-[Danuka Lashan](Danuka.21@cse.mrt.ac.lk)

