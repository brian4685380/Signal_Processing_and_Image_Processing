import numpy as np
from matplotlib import pyplot as plt

const = 0.2
k1 = 0.2
k2 = 5
L = 10
C = np.zeros(101, dtype=np.float64)
x = np.zeros(101)
y = np.zeros(101)
for i in range(51):
    x[i] = 1

noise = (np.random.rand(101) - 0.5) * const
x = x + noise

for i in range (101):
    sum = 0
    for j in range(max(i - L, 0), min(i + L , 100) + 1):
        sum += np.exp(-k1 * (i - j) ** 2) * np.exp(-k2 * (x[j] - x[i]) ** 2)
    C[i] = 1 / sum 
for i in range (101):
    sum = 0
    for j in range(max(i - L, 0), min(i + L , 100) + 1):
        sum += x[j] * np.exp(-k1 * (i - j) ** 2) * np.exp(-k2 * (x[j] - x[i]) ** 2)
    y[i] = C[i] * sum

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x)
ax1.set_title('Plot of x')

ax2.plot(y)
ax2.set_title('Plot of y')

plt.show()