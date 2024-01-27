import numpy as np
import matplotlib.pyplot as plt


def conv (img, filter):
    x, y = img.shape
    w, h = filter.shape
    img1 = np.zeros((x - w + 1, y - h + 1), dtype = np.float64)
    for i in range(x - w + 1):
        for j in range(y - h + 1):
            img1[i][j] = abs(np.sum(img[i:i + w, j:j + h] * filter)) / 255 
    return img1

image = plt.imread('../Pic/Lena_gray_512.bmp')
image = image.astype(np.float64)
k = np.zeros((21, 21))
k = k.astype(np.float64)
for i in range (21):
    for j in range (21):
        k[i][j] = np.exp(-0.1 * ((i - 10) ** 2 + (j - 10) ** 2))
k = k / k.sum()

y = conv(image, k)
noise = np.random.rand(y.shape[0], y.shape[1])
y += (noise * 0.1)

plt.imshow(y, cmap='gray')
plt.show()

C = 0.3
K = np.fft.fft2(k)
H = np.zeros((21, 21))

for i in range (21):
    for j in range (21):
        H[i][j] = 1 / (C / np.conjugate(K [i][j]) + K[i][j])

h = np.fft.ifft2(H)
h = np.abs(h)

result = conv(y, h)
plt.imshow(result, cmap='gray')
plt.show()