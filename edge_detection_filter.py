import numpy as np
import matplotlib.pyplot as plt

def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

an = 0.1
sigma = 1
L = 10
n1 = np.arange(-30, 101)
n2 = np.arange(-L, L + 1)
n3 = np.arange(-30 - L, 100 + L + 1)
x = np.zeros_like(n1)
h = np.zeros_like(n2)
y = np.zeros_like(n3)
h = h.astype(np.float64)
y = y.astype(np.float64)
sum = 0
for i in range(L) : 
    sum += np.exp(-sigma * i)
C = 1 / sum
for i in range(len(n2)) :
    h[i] = C * np.exp( -sigma * abs(n2[i])) * sgn(n2[i])
    print(h[i])

x[(n1 >= -10) & (n1 <= 20) | (n1 >= 50) & (n1 <= 80)] = 1
noise = an * (np.random.rand(131) - 0.5)
x1 = x + noise

y = np.convolve(x1, h)

# plt.stem(n1, x1)
# plt.stem(n2, h)
plt.stem(n3, y)
plt.show()