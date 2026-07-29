import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 200]

plt.plot(months, sales)

plt.xlabel("Months")
plt.ylabel("Sales")

plt.title("Monthly Sales")

plt.show()
