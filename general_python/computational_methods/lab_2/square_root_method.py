import numpy as np


class SquareRootMethod:

    @staticmethod
    def get_matrix_decomposition(matrix: np.ndarray):
        order = matrix.shape[0]
        d_vector = np.array([])
        s_matrix = np.zeros((order, order), dtype=np.float)

        for i in range(order):
            d_vector = np.insert(d_vector, i, np.sign(
                matrix[i, i] - np.sum((s_matrix[:i, i] ** 2) * d_vector[:i])))

            s_matrix[i, i] = np.sqrt(d_vector[i] * (
                    matrix[i, i] - np.sum((s_matrix[:i, i] ** 2) * d_vector[:i])))

            for j in range(i + 1, order):
                s_matrix[i, j] = (matrix[i, j] - np.sum(s_matrix[:i, i] * d_vector[:i] * s_matrix[:i, j])) \
                                 / (d_vector[i] * s_matrix[i, i])

        return s_matrix, d_vector

    @staticmethod
    def get_equation_solution(systems_matrix: np.ndarray,
                              free_elements_vector: np.ndarray):
        pass

    @staticmethod
    def get_determinant(matrix: np.ndarray):
        pass

    @staticmethod
    def get_reversed_matrix(matrix: np.ndarray):
        pass
