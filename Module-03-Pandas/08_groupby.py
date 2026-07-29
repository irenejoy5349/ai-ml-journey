import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Employee": ["Ram", "John", "Sam", "Alex", "Bob"],
    "Salary": [50000, 60000, 70000, 55000, 65000]
}

df = pd.DataFrame(data)

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Salary"].sum())
