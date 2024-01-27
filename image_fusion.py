import numpy as np
import matplotlib.pyplot as plt

image1 = plt.imread('../Pic/gray512/Lena.bmp')
image2 = plt.imread('../Pic/gray512/zelda.bmp')

fft1 = np.fft.fft2(image1)
fft2 = np.fft.fft2(image2)

mergedfft = np.zeros((512, 512), dtype=complex)
for i in range(512):
    for j in range(512):
        if (i - 256) ** 2 + (j - 256) ** 2 < 335 ** 2: 
            # > to choose low frequency part of image 1, otherwise choose low frequency part of image 2
            mergedfft[i][j] = fft1[i][j]
        else:
            mergedfft[i][j] = fft2[i][j]
merged = np.fft.ifft2(mergedfft)
merged = np.abs(merged)
plt.imshow(merged, cmap='gray')
plt.show()
