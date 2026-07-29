import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [50, 55, 65, 70, 80, 90]

plt.scatter(hours, scores)

plt.xlabel("Study Hours")
plt.ylabel("Scores")

plt.title("Study Hours vs Scores")

plt.show()
