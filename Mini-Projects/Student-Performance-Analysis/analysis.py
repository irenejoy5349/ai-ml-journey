import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("student_data.csv")

print(df.head())

print(df.shape)

print(df.info())

print(df.describe())
