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
    def get_equation_solution(matrix: np.ndarray, free_vector: np.ndarray):
        order = matrix.shape[0]

        if (matrix.T != matrix).any():
            free_vector = np.matmul(matrix.T, free_vector)
            matrix = np.matmul(matrix.T, matrix)

        s, d = SquareRootMethod.get_matrix_decomposition(matrix)

        y = np.array([])
        for i in range(order):
            y = np.insert(y, i, (free_vector[i] - np.sum(y[:i] * s[:i, i])) / s[i, i])

        x = np.array([])
        for i in range(order - 1, -1, -1):
            x = np.insert(x, 0, (y[i] - np.sum(s[i, i+1:] * d[i] * x))
                          / (s[i, i] * d[i]))

        return x

    @staticmethod
    def get_determinant(matrix: np.ndarray):
        not_symmetric = (matrix.T != matrix).any()

        if not_symmetric:
            matrix = np.matmul(matrix.T, matrix)

        s, d = SquareRootMethod.get_matrix_decomposition(matrix)

        determinant = np.prod(s.diagonal() ** 2) * np.prod(d)

        return np.sqrt(determinant) if not_symmetric else determinant
