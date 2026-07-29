import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 30, 40, 50]

sns.lineplot(x=range(5), y=data)

plt.title("Seaborn Line Plot")

plt.show()
