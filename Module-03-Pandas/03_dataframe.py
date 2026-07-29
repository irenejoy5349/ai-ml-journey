import pandas as pd

data = {
    "Name": ["Ram", "John", "Sam"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}

df = pd.DataFrame(data)

print(df)

print(df.head())

print(df.shape)

print(df.columns)
