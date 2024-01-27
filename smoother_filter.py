import numpy as np
import matplotlib.pyplot as plt

L = 10
sigma = 0.1
an = 1
n1 = np.arange(-50, 101)
n2 = np.arange(-L, L + 1)
n3 = np.arange(-L -50, 100 + L + 1)
x = np.zeros_like(n1)
h = np.zeros_like(n2)
y = np.zeros_like(n3)
x = x.astype(np.float64)
h = h.astype(np.float64)
y = y.astype(np.float64)
noise = an * (np.random.rand(151) - 0.5)
sum = 0
for i in range(len(n2)):
    sum += np.exp(-sigma * abs(n2[i]))
C = 1 / sum

for i in range(len(n2)):
    h[i] = C * np.exp(-sigma * abs(n2[i]))
    print(n2[i], np.exp(-sigma * abs(n2[i])))
for i in range(len(n1)):
    x[i] = n1[i] * 0.1
x1 = x + noise
y = np.convolve(x1, h)

# plt.stem(n1, x1)
# plt.show()
# plt.stem(n2, h)
# plt.show()
plt.stem(n3, y)
plt.show()