from single_division import SingleDivision
import numpy as np

if __name__ == "__main__":
    a = np.array([[1, 2, 3], [5, 2, 1],  [6, 6, 2]], dtype=float)
    print(np.matmul(SingleDivision.get_reversed_matrix(a), a))
