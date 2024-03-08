import numpy as np

T = np.array(
    [[0.2, 0.3, 0.2],
     [0.4, 0.1, 0.2],
     [0.1, 0.3, 0.2]]
)

A = np.identity(3) - T

A_inv = np.linalg.inv(A)

A_inv_should_be = 1 / 0.384 * np.array(
    [[0.66, 0.30, 0.24],
     [0.34, 0.62, 0.24],
     [0.21, 0.27, 0.60]]
)

assert np.allclose(A_inv, A_inv_should_be, atol=1e-2)

print("All tests passed!")
