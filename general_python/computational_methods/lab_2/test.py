from square_root_method import SquareRootMethod
import numpy as np

if __name__ == "__main__":
    test_matrix = np.array([[1, 4, 3],
                            [4, 5, 6],
                            [3, 6, 1]])
    f = np.array([1, 2, 3])
    print(np.matmul(test_matrix, SquareRootMethod.get_equation_solution(test_matrix, f)))
