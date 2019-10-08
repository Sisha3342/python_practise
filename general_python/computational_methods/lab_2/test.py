from square_root_method import SquareRootMethod
import numpy as np

if __name__ == "__main__":
    test_matrix = np.array([[1, 2, 3],
                            [2, 5, 6],
                            [3, 6, 1]])
    a = np.array([1, 2, 3])
    s, d = SquareRootMethod.get_matrix_decomposition(test_matrix)

    print(SquareRootMethod.get_determinant(test_matrix))
