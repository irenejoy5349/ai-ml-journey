import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Watch"]
sales = [50, 80, 40, 60]

plt.bar(products, sales)

plt.xlabel("Products")
plt.ylabel("Sales")

plt.title("Product Sales")

plt.show()
