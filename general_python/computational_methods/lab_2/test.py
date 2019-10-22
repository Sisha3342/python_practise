from square_root_method import SquareRootMethod
import numpy as np

if __name__ == "__main__":
    test_matrix = np.array([[8.30, 3.82, 4.10, 1.90],
                            [3.92, 8.45, 6.58, 2.46],
                            [3.77, 8.41, 8.04, 2.28],
                            [2.21, 2.45, 1.69, 6.99]])
    f = np.array([-9.45, 12.21, 14.25, -8.35])

    print(SquareRootMethod.get_determinant(test_matrix))
