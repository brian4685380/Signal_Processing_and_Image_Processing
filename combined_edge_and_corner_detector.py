import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import convolve2d

sigma = 3
k = 0.05

image = plt.imread('../Pic/gray512/Lena.bmp')

def gaussian(x, y, sigma):
    return np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2)) / (2 * np.pi * sigma ** 2)

# Define the kernel for X and Y convolution as 2D arrays
kernel_x = np.array([[-1, 0, 1]])
kernel_y = np.array([[-1], [0], [1]])

# Perform 2D convolution to calculate X and Y gradients
X = convolve2d(image, kernel_x, mode='same', boundary='wrap')
Y = convolve2d(image, kernel_y, mode='same', boundary='wrap')

X2 = X**2  # Square each element
Y2 = Y**2
XY = X * Y  # Element-wise multiplication

# Now you can use X2, Y2, and XY for further calculations

w = np.zeros((11, 11))
for i in range(11):
    for j in range(11):
        w[i, j] = gaussian(i - 5, j - 5, sigma)

A = convolve2d(X2, w, mode='same', boundary='wrap')
B = convolve2d(Y2, w, mode='same', boundary='wrap')
C = convolve2d(XY, w, mode='same', boundary='wrap')

Det = A * B - C ** 2
Trace = A + B

R = Det - k * Trace ** 2

plt.imshow(R, cmap='gray')
plt.show()
