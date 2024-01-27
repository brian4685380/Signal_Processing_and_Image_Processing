import numpy as np
import matplotlib.pyplot as plt


image = np.zeros((255, 255))
for i in range (0, 255):
    image[0:255, i] = i / 255

plt.imshow(image, cmap='gray')
plt.show()