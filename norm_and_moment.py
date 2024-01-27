import numpy as np
import matplotlib.pyplot as plt


x = np.zeros((100, 100))
for i in range (100) :
    for j in range (100) :
        if ((j - 30) ** 2 + (i - 50) ** 2) ** 0.5 + ((j - 70) ** 2 + (i - 50) ** 2) ** 0.5 <= 80:
            x[i][j] = 1
plt.imshow(x, cmap='gray', vmin = 0, vmax = 1)
plt.show()

L0_norm = x.sum()
L1_norm = x.sum()
L2_norm = (x ** 2).sum() ** 0.5
Linf_norm = x.max()
print(L0_norm, L1_norm, L2_norm, Linf_norm)

nbar_x = 0
nbar_y = 0
for i in range (100) :
    for j in range (100) :
        nbar_x += j * x[i][j]
        nbar_y += i * x[i][j]
nbar_x /= x.sum()
nbar_y /= x.sum()

a = 0
b = 2
central_moment = 0
for i in range (100) :
    for j in range (100) :
        central_moment += ((j - nbar_x) ** a) * ((i - nbar_y) ** b) * float(x[i][j])
central_moment /= x.sum()

print(central_moment)
# import numpy as np

# def is_integer(value):
#     return int(value) == value

# x0 = 0
# y0 = 0
# rx = 10
# ry = 8

# x_range = np.arange(x0 - rx, x0 + rx + 1)
# y_range = np.arange(-ry, ry + 1)
# X, Y = np.meshgrid(x_range, y_range)

# ellipse_equation = ry**2 * (1 - ((X - x0)**2 / rx**2)) - Y**2

# integer_points_mask = (ellipse_equation >= 0) & (np.vectorize(is_integer)(Y))

# x_coordinates = X[integer_points_mask]
# y_coordinates = Y[integer_points_mask]
# d = np.zeros_like(x_coordinates)

# for i in range(len(x_coordinates)) :
#     d[i] = (x_coordinates[i] ** 2 + y_coordinates[i] ** 2) ** 0.5

# #find norm for d 

