# For Loop

for i in range(1, 6):
    print(i)

print("----------------")

# While Loop

num = 1

while num <= 5:
    print(num)
    num += 1

print("----------------")

# Break

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("----------------")

# Continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
