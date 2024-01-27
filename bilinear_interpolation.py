import numpy as np
import matplotlib.pyplot as plt
from math import floor

image = plt.imread('../Pic/gray512/lena.bmp')
m, n = image.shape
M = floor(1.5 * m)
N = floor(1.6 * n)
new_image = np.zeros((M, N))

for i in range(M):
    for j in range(N):
        m0 = i * m / M
        n0 = j * n / N

        if m0 > m - 1:
            m0 = m - 2
        if n0 > n - 1:
            n0 = n - 2

        a = m0 - floor(m0)
        b = n0 - floor(n0)

        new_image[i][j] = (1 - a) * (1 - b) * image[floor(m0)][floor(n0)] + \
                          a * (1 - b) * image[floor(m0) + 1][floor(n0)] + \
                          (1 - a) * b * image[floor(m0)][floor(n0) + 1] + \
                          a * b * image[floor(m0) + 1][floor(n0) + 1]

fig, axs = plt.subplots(1, 2)

axs[0].imshow(image, cmap='gray')
axs[0].set_title('Original Image')

axs[1].imshow(new_image, cmap='gray')
axs[1].set_title('Bilinear Interpolation')

plt.show()
