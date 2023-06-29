import numpy as np

n_array = np.array([1, 0, 2, 0, 3, 0, 0, 5, 6, 7, 5, 0, 8])

res = np.where(n_array == 0)[0]

print(res.sum( ))