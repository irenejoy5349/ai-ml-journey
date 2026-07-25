# Lists

fruits = ["apple", "banana", "mango"]

print(fruits)

print("----------------")

# Indexing
print(fruits[0])
print(fruits[-1])

print("----------------")

# Append
fruits.append("orange")
print(fruits)

print("----------------")

# Insert
fruits.insert(1, "grapes")
print(fruits)

print("----------------")

# Remove
fruits.remove("banana")
print(fruits)

print("----------------")

# Pop
fruits.pop()
print(fruits)

print("----------------")

# Update
fruits[1] = "kiwi"
print(fruits)

print("----------------")

# Length
print(len(fruits))

print("----------------")

# Sort
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)

print("----------------")

# Reverse
numbers.reverse()
print(numbers)

print("----------------")

# Count
items = ["apple", "banana", "apple", "mango"]
print(items.count("apple"))

print("----------------")

# Index
print(items.index("banana"))

print("----------------")

# Copy
new_list = items.copy()
print(new_list)

print("----------------")

# Clear
new_list.clear()
print(new_list)
