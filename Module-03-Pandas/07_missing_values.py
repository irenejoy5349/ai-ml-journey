import pandas as pd
import numpy as np

data = {
    "Name": ["Ram", "John", "Sam"],
    "Age": [25, np.nan, 35],
    "Score": [85, 90, np.nan]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())

print(df.isnull().sum())

df_clean = df.dropna()

print(df_clean)

df_fill = df.fillna(0)

print(df_fill)
