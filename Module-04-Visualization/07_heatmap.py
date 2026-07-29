import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Math": [80, 90, 70, 60],
    "Science": [85, 95, 75, 65],
    "English": [75, 85, 80, 70]
}

df = pd.DataFrame(data)

correlation = df.corr()

sns.heatmap(correlation, annot=True)

plt.title("Feature Correlation Heatmap")

plt.show()
