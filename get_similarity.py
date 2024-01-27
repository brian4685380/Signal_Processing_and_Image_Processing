import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log10

def nrmse(x, y):
    sum1 = sum2 = 0
    m, n = x.shape
    for i in range(m):
        for j in range(n):
            sum1 += (y[i][j] - x[i][j]) ** 2
            sum2 += x[i][j] ** 2
    return sqrt(sum1 / sum2)
def psnr(x, y):
    sum = 0
    m, n = x.shape
    xmax = x.max()
    for i in range(m):
        for j in range(n):
            sum += (y[i][j] - x[i][j]) ** 2
    return 10 * log10(xmax ** 2 / (sum / (m * n)))
                      
def psnr_color(x, y):
    m, n, _ = x.shape
    xmax = x.max()
    for i in range(m):
        for j in range(n):
            for k in range(3):
                sum += (y[i][j][k] - x[i][j][k]) ** 2
    return 10 * log10(xmax ** 2 / (sum / (m * n * 3)))
def ssim(x, y):
    mu_x = x.mean()
    mu_y = y.mean()
    var_x = x.var()
    var_y = y.var()
    cov = np.cov(x.flatten(), y.flatten())[0][1]
    L = x.max() - x.min()
    c1 = sqrt(1 / L)
    c2 = sqrt(1 / L)
    return (2 * mu_x * mu_y + (c1 * L) ** 2) * (2 * cov + (c2 * L) ** 2) / ((mu_x ** 2 + mu_y ** 2 + (c1 * L) ** 2) * (var_x + var_y + (c2 * L) ** 2))


image1 = plt.imread('../Pic/LENA.bmp')
image2 = plt.imread('../Pic/Lena1.bmp')

print (nrmse(image1, image2), psnr(image1, image2), ssim(image1, image2))