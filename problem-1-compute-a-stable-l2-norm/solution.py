import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    s = max(x)
    x = np.array(x)/s
    grad = s*(np.sum(x ** 2) ** 0.5)
    return grad
