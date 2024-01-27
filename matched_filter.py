import numpy as np
import matplotlib.pyplot as plt

H = 1
n1 = np.arange(0, 221)
n2 = np.arange(0, 21)
n3 = np.arange(0, 241)
x = np.zeros_like(n1)
h = np.zeros_like(n2)
y = np.zeros_like(n3)
x = x.astype(np.float64)
h = h.astype(np.float64)
y = y.astype(np.float64)

sum = 0
for i in range (len(n2)) :
    h[i] = (10 - i) / 10 * H
    sum += h[i] ** 2
for i in range (len(n2)) :
    h[i] /= sum ** 0.5
for i in range (20, 41) :
    x[i] = H
for i in range (70, 91) :
    x[i] = (i - 80) / 10 * H
for i in range (120, 141) :
    x[i] = (130 - i) / 10 * H
for i in range (170, 191) :
    x[i] = np.sin((180 - i) / 10 * np.pi) * H
y = np.convolve(x, h)
norm = 0
for i in range (0, 21) :
    norm += x[i] ** 2
    y[i] /= norm ** 0.5
for i in range (21, 221) :
    norm += x[i] ** 2 - x[i - 21] ** 2
    y[i] /= norm ** 0.5
for i in range (221, 241) :
    norm -= x[i - 21] ** 2
    y[i] /= norm ** 0.5
plt.stem(n1, x, markerfmt=' ')
plt.show()
plt.stem(n2, h, markerfmt=' ')
plt.show()
plt.stem(n3, y, markerfmt=' ')
plt.show()