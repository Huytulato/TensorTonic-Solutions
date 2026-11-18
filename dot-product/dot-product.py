import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # tính tích vô hướng với đầu vào là 2 vecto x và y
    x = np.asarray(x, dtype = float)
    y = np.asarray(y, dtype = float)
    return float(np.dot(x, y))