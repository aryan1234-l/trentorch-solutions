import numpy as np


def solve(f, samples):
    # TODO: Return the mean of f applied to the samples.
    return np.mean(np.array(list(map(f, samples))))
