import numpy as np
import matplotlib.pyplot as plt

def erosion (image) :
    h, w = image.shape
    erosion = np.zeros((h, w), dtype=np.uint8)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            erosion[i][j] = image[i][j] & image[i - 1][j] & image[i][j - 1] & image[i][j + 1] & image[i + 1][j]
    return erosion

def dilation (image) :
    h, w = image.shape
    dilation = np.zeros((h, w), dtype=np.uint8)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            dilation[i][j] = image[i][j] | image[i - 1][j] | image[i][j - 1] | image[i][j + 1] | image[i + 1][j]
    return dilation

image = plt.imread('../Pic/binary_img/binary22.bmp')
image = image.mean(axis=2).astype(np.uint8)

for i in range(5):
    image = erosion(image)
for i in range(5):
    image = dilation(image)

plt.imshow(image, cmap='gray')
plt.show()
