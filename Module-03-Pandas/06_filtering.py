import pandas as pd

data = {
    "Name": ["Ram", "John", "Sam", "Alex"],
    "Age": [25, 30, 35, 20],
    "Score": [85, 90, 95, 70]
}

df = pd.DataFrame(data)

print(df[df["Age"] > 25])

print(df[df["Score"] >= 90])

print(df[(df["Age"] > 20) & (df["Score"] > 80)])
