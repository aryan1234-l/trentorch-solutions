import numpy as np


def solve(x):
    """Implement ReLU Activation from the mathematical contract in README.md."""
    return np.maximum(np.asarray(x), 0)
