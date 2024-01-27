import matplotlib.pyplot as plt
import numpy as np

# def diff (img, bound = 50):
#     x, y = img.shape
#     img1 = np.zeros((x, y), dtype = np.float32)
#     for i in range(x):
#         for j in range(1, y):
#             img1[i][j] = abs(float(img[i][j]) - float(img[i][j - 1])) / 255
#     return img1


def conv(img, filter, magnify=1):
    x, y = img.shape
    w, h = filter.shape
    img1 = np.zeros((x - w + 1, y - h + 1), dtype=np.float32)
    for i in range(x - w + 1):
        for j in range(y - h + 1):
            img1[i][j] = abs(
                np.sum(img[i:i + w, j:j + h] * filter)) / 255 * magnify
    return img1


image = plt.imread('../Pic/lena_128.bmp')
horizontal_sobel = np.array([[1 / 4, 0, -1 / 4],
                            [2 / 4, 0, -2 / 4],
                            [1 / 4, 0, -1 / 4]])
vertical_sobel = np.array([[1 / 4, 2 / 4, 1 / 4],
                           [0, 0, 0],
                           [-1 / 4, -2 / 4, -1 / 4]])
slope1_sobel = np.array([[0, -1 / 4, -2 / 4],
                         [1 / 4, 0, -1 / 4],
                         [2 / 4, 1 / 4, 0]])
slopeneg1_sobel = np.array([[-2 / 4, -1 / 4, 0],
                           [-1 / 4, 0, 1 / 4],
                           [0, 1 / 4, 2 / 4]])

laplacian = np.array([[-1 / 8, -1 / 8, -1 / 8],
                     [-1 / 8, 1, -1 / 8],
                     [-1 / 8, -1 / 8, -1 / 8]])

difmatrix = np.array([[-1, 1]])

# use conv() to calculate the filtered image diff to directly calculate the difference and get margin

result = conv(image, difmatrix, 1.5)
# result = diff(image, 30)
plt.imshow(result, cmap='gray', vmin=0, vmax=1)
plt.show()
