import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi, floor

image = plt.imread('../Pic/gray512/lena.bmp')
transformed = np.zeros_like(image, dtype=np.float64)

cn = cm = 256
a = 1
b = 0
c = 0.3
d = 1
scale = a * d - b * c
for i in range (512) :
    for j in range (512) :
        m = (d * (i - cm) - b * (j - cn)) / scale + cm
        n = (-c * (i - cm) + a * (j - cn)) / scale + cn
        if (m >= 0 and m < 511 and n >= 0 and n < 511) :
            m0 = floor(m)
            n0 = floor(n)
            a1 = m - m0
            b1 = n - n0
            transformed[i][j] = (1 - a1) * (1 - b1) * image[m0][n0] + a1 * (1 - b1) * image[m0 + 1][n0] + (1 - a1) * b1 * image[m0][n0 + 1] + a1 * b1 * image[m0 + 1][n0 + 1]

plt.imshow(transformed, cmap='gray')
plt.show()