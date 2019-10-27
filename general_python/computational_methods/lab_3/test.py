import simple_iterations as si
import numpy as np


if __name__ == "__main__":
    # test_matrix = np.array([[1, -2, 3],
    #                         [2, -3, -2],
    #                         [1, 2, 3]])
    #
    # x_array = np.array([1, 2, 3])
    # f = np.matmul(test_matrix, x_array)
    #
    # si_ = si.SimpleIterations(test_matrix, f, 0.00001)
    # print(si_.get_solution())

    test_matrix = np.array([[8.30, 3.82, 4.10, 1.90],
                            [3.92, 8.45, 6.58, 2.46],
                            [3.77, 8.41, 8.04, 2.28],
                            [2.21, 2.45, 1.69, 6.99]])

    # 4th row is dominated

    # step_1
    test_matrix[1, :] -= test_matrix[0, :] * 3.92 / 8.30
    # step 2
    test_matrix[0, :] -= test_matrix[1, :]
    # step 3
    test_matrix[2, :] -= 3.77 / 8.3 * test_matrix[0, :]
    # step 4
    test_matrix[2, :] -= test_matrix[2, 1] / test_matrix[1, 1] * test_matrix[1, :]
    print(test_matrix)
