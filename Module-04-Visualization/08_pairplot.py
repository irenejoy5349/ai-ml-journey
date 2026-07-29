import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Height": [150, 160, 170, 180, 190],
    "Weight": [50, 60, 70, 80, 90],
    "Age": [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

sns.pairplot(df)

plt.show()
