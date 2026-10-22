import numpy as np


def solve(x):
    """Implement Logistic Sigmoid from the mathematical contract in README.md."""
    x = np.array(x)
    x = 1/(1+np.exp(-x))
    return x
