from single_division import SingleDivision
import numpy as np

if __name__ == "__main__":
    a = np.array([[1, 2, 4], [3, 1, 1],  [2, 3, 3]], dtype=float)
    f = np.array([2, 3, 4], dtype=float)[:, np.newaxis]

    print(np.matmul(a, SingleDivision.get_reversed_matrix(a)))
