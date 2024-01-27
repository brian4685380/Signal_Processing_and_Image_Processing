import numpy as np

A = np.array([[2, -1, 3], [-1, 3, 5], [0, 2, 4], [4, -2, -1], [1, 0, 4], [-2, 5, 5]])
U, S, Vh = np.linalg.svd(A, full_matrices=True)

print(U)
print(S)
print(Vh)