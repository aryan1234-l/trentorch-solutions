# Anomaly Z-Score

Advanced | problemset | unsupervised-ml | anomaly-detection

Flag anomalies by z-score. Standardise `x` with its mean and **population** standard deviation (column-wise for a 2-D array) and mark every entry whose absolute z-score is strictly greater than `threshold` (default $3$). A constant column has z-score $0$ everywhere.

Implement `solve(x, threshold=3)`.

**Returns.** Return a boolean NumPy array of the same shape as `x`.

### Examples

**Example 1**

Input:

```python
solve([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 50.0], 2.5)
```

Output:

```text
[False, False, False, False, False, False, False, False, False, True]
```

**Example 2**

Input:

```python
solve([[1.0, 5.0], [2.0, 5.0], [3.0, 5.0]], 1.0)
```

Output:

```text
[[True, False], [False, False], [True, False]]
```
