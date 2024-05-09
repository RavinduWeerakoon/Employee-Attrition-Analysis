import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler



marvellous = pd.read_csv("employees.csv")

marvellous.drop(["Employee_No","Employee_Code","Name", "Title"], axis=1, inplace=True)

marvellous["Year_of_Birth"] = marvellous["Year_of_Birth"].replace("'0000'", np.nan)
marvellous["Year_of_Birth"] = pd.to_numeric(marvellous["Year_of_Birth"], errors='coerce')

marvellous['Date_Joined'] = pd.to_datetime(marvellous['Date_Joined'], errors='coerce')
marvellous['Date_Resigned'] = pd.to_datetime(marvellous['Date_Resigned'], errors='coerce')
marvellous['Inactive_Date'] = pd.to_datetime(marvellous['Inactive_Date'], errors='coerce')

ages_in_the_company = (marvellous['Date_Resigned'] - marvellous['Date_Joined']).dt.days / 365
ages_in_the_company = ages_in_the_company.fillna((pd.to_datetime('2023-01-01') - marvellous['Date_Joined']).dt.days / 365)

marvellous["ages_in_the_company"] = ages_in_the_company
marvellous.drop(["Date_Joined", "Date_Resigned","Inactive_Date"], axis=1, inplace=True)
z = np.where((marvellous["Reporting_emp_1"] != "\\N") | (marvellous["Reporting_emp_2"] != "\\N"), 1,0)
marvellous["reported"] = z

marvellous.drop(["Reporting_emp_1","Reporting_emp_2", "Religion_ID"], axis=1, inplace=True)



Gender_map = {"Male":1, "Female":0}
Status_map = {"Inactive":0, "Active":1}
Employment_Category_map = {"Labour":1, "Staff":2, "Management":3}
marvellous["Gender"] = marvellous["Gender"].map(Gender_map)
marvellous["Status"] = marvellous["Status"].map(Status_map)
marvellous["Employment_Category"] = marvellous["Employment_Category"].map(Employment_Category_map)
marvellous["Marital_Status"] = marvellous["Marital_Status"].map({"Married":0, "Single":1})


one_hot = pd.get_dummies(marvellous["Employment_Type"], prefix="Employment_Type")
marvellous = pd.concat([marvellous, one_hot], axis=1)


one_hot = pd.get_dummies(marvellous["Religion"], prefix="Religion")
marvellous = pd.concat([marvellous, one_hot], axis=1)


# Create a copy of the dataframe
df = marvellous.copy().drop(["Employment_Type", "Religion", "Designation"], axis=1)
temp_df = marvellous.copy().drop(["Employment_Type", "Religion", "Designation"], axis=1)


imputer = KNNImputer(n_neighbors=2)
df.loc[:, :] = imputer.fit_transform(temp_df)

marvellous["Year_of_Birth"] = df["Year_of_Birth"].astype(int)
marvellous["Marital_Status"] = df["Marital_Status"]


scaler = MinMaxScaler()

# Fit and transform the Year_of_Birth, ages_in_the_company, and Net Salary columns
marvellous["Year_of_Birth"] = scaler.fit_transform(marvellous["Year_of_Birth"].values.reshape(-1, 1))
marvellous["ages_in_the_company"] = scaler.fit_transform(marvellous["ages_in_the_company"].values.reshape(-1, 1))

marvellous.to_csv("employee_preprocess_18.csv", index=False)