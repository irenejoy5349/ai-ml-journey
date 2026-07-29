import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("student_data.csv")

print(df.head())

print(df.shape)

print(df.info())

print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())

df["Average_Score"] = (
    df["Math_Score"] +
    df["Science_Score"] +
    df["English_Score"]
) / 3


print("\nData with Average Score:")
print(df)

plt.figure(figsize=(6,4))

sns.scatterplot(
    x="Study_Hours",
    y="Average_Score",
    data=df
)

plt.title("Study Hours vs Average Score")

plt.xlabel("Study Hours")

plt.ylabel("Average Score")

plt.show()

plt.figure(figsize=(6,4))

sns.histplot(
    df["Average_Score"],
    bins=5,
    kde=True
)

plt.title("Average Score Distribution")

plt.xlabel("Average Score")

plt.ylabel("Number of Students")

plt.show()

plt.figure(figsize=(8,5))

correlation = df.corr(numeric_only=True)

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Feature Correlation Heatmap")

plt.show()

print("\nTop Student:")

top_student = df.loc[df["Average_Score"].idxmax()]

print(top_student)


print("\nAverage Score:")

print(df["Average_Score"].mean())


print("\nAverage Study Hours:")

print(df["Study_Hours"].mean())
