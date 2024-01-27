import numpy as np
import matplotlib.pyplot as plt

def rgb2ycbcr(rgb_image):
    rgb_image = rgb_image.astype(np.float32)
    transform_matrix = np.array([[0.299, 0.587, 0.114],
                                 [-0.169, -0.331, 0.5],
                                 [0.5, -0.419, -0.081]])
    ycbcr_image = np.zeros(shape=rgb_image.shape)
    w, h, _ = rgb_image.shape
    for i in range(w):
        for j in range(h):
            ycbcr_image[i, j, :] = np.dot(transform_matrix, rgb_image[i, j, :])
    return ycbcr_image

def ycbcr2rgb(ycbcr_image):
    ycbcr_image = ycbcr_image.astype(np.float32)
    transform_matrix = np.array([[0.299, 0.587, 0.114],
                                 [-0.169, -0.331, 0.5],
                                 [0.5, -0.419, -0.081]])
    transform_matrix_inv = np.linalg.inv(transform_matrix)
    rgb_image = np.zeros(shape=ycbcr_image.shape)
    w, h, _ = ycbcr_image.shape
    for i in range(w):
        for j in range(h):
            rgb_image[i, j, :] = np.dot(transform_matrix_inv, ycbcr_image[i, j, :])
    return rgb_image.astype(np.float64)
def darkenAndLighten(ycbcr_image, alpha=1):
    w, h, _ = ycbcr_image.shape
    for i in range(w):
        for j in range(h):
            ycbcr_image[i][j][0] = 255 * (ycbcr_image[i][j][0] / 255) ** alpha

image = plt.imread('../Pic/baboon1.bmp')
ycbcr = rgb2ycbcr(image)
darkenAndLighten(ycbcr, 2)

new_image = ycbcr2rgb(ycbcr)

fig, axs = plt.subplots(1, 2)

axs[0].imshow(image)
axs[0].set_title('Original Image')

axs[1].imshow(new_image/255)
axs[1].set_title('Lighten / Darken Image')

plt.show()

