import pandas as pd
# data uploading----
df=pd.read_csv(r"C:\Users\manis\Downloads\Messy_data.csv").head(100)

# view data----
# print(df.head(20))


# data cleaning~~~~~

# missing values---
# print("missing value :",df.isnull().sum())

# remove missing values
# print("removed missing value rows",df.dropna())
# df = df.dropna()

# print("remove colomuns",df.dropna(axis=1))

"""  fill missing values"""
num_cols=df.select_dtypes(include=["number"]).columns
df[num_cols]=df[num_cols].fillna(0)

'''fill string columns with unknown'''

str_cols=df.select_dtypes(include=["object","string"]).columns
df[str_cols]=df[str_cols].fillna("unknown")



# data infromation----
# print(df.info())

# check duplicate coloumn--
print("duplicate value",df.duplicated().sum())

df=df.drop_duplicates()

df.rename(columns={"Name":"Student_Name"}, inplace=True)
df.drop("Date Recorded", axis=1, inplace=True)
df.replace({"Male":"M", "Female":"F"}, inplace=True)
df["Location"] = df["Location"].str.strip()



# find outlier
Q1 = df["Monthly Salary (INR)"].quantile(0.25)
Q3 = df["Monthly Salary (INR)"].quantile(0.75)

IQR = Q3 - Q1

outliers = df[(df["Monthly Salary (INR)"] < Q1 - 1.5*IQR) |
              (df["Monthly Salary (INR)"] > Q3 + 1.5*IQR)]

print(outliers)