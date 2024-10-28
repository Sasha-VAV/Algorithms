import numpy as np
A = np.array([
    [1, 4, -3],
    [4, 2, 1],
    [1, -1, 0]]
)
B = np.array([
    3,
    11,
    1
])

C = np.linalg.solve(A, B)
print(C)
print(A@C)