import numpy as np

print(np.random.rand())

print(np.random.rand(3))

print(np.random.randint(1, 10))

print(np.random.randint(1, 10, size=5))

a = np.array([10, 20, 30, 40, 50])

np.random.shuffle(a)

print(a)
