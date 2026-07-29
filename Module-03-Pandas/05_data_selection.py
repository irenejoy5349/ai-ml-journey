import pandas as pd

data = {
    "Name": ["Ram", "John", "Sam"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}

df = pd.DataFrame(data)

print(df["Name"])

print(df[["Name", "Score"]])

print(df.loc[0])

print(df.iloc[1])
