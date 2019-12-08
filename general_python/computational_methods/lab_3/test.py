import simple_iterations as si
from JacobiMethod import JacobiMethod as jm
from GaussSeidel import GaussSeidel as gs
import numpy as np


if __name__ == "__main__":
    test_matrix = np.array([[8.30, 3.82, 4.10, 1.90],
                            [5.92, 8.45, 8.58, 2.46],
                            [3.77, 6.41, 8.04, 2.28],
                            [2.21, 4.45, 1.69, 6.99]])

    f = np.array([-11.45, 12.21, 16.25, -8.35])

    si_ = si.SimpleIterations(test_matrix, f, 1e-05)
    print(si_.get_solution())

    # 4th row is dominated
    # step_1
    # test_matrix[2, :] -= test_matrix[1, :]
    # f[2] -= f[1]
    # step 2
    # test_matrix[0, :] = 2 * test_matrix[0, :] - test_matrix[1, :]
    # f[0] = 2 * f[0] - f[1]
    # step 3
    # test_matrix[1, :] -= 4 * test_matrix[2, :]
    # f[1] -= 4 * f[2]

    test_matrix[0] = 2*test_matrix[0] - test_matrix[1]
    f[0] = 2 * f[0] - f[1]
    test_matrix[3] = 2*test_matrix[3] - test_matrix[1]
    f[3] = 2*f[3] - f[1]
    test_matrix[2] = 3*test_matrix[2] - 2*test_matrix[1]
    f[2] = 3*f[2] - 2*f[1]
    test_matrix[1] = 2*test_matrix[1] - test_matrix[0] - test_matrix[2]
    f[1] = 2*f[1] - f[0] - f[2]

    # print(jm.get_solution(test_matrix, f, 1e-05))
    # print(gs.get_solution(test_matrix, f, 1e-05))


