import numpy as np


class SingleDivision:

    @staticmethod
    def get_equation_solution(matrix: np.ndarray, f_vector: np.ndarray):
        matrix_copy = matrix.copy()
        f_vector_copy = f_vector.copy()
        order = matrix_copy.shape[0]

        for i in range(order):
            f_vector_copy[i] /= matrix_copy[i, i]
            matrix_copy[i] /= matrix_copy[i, i]

            for j in range(i + 1, order):
                f_vector_copy[j] -= matrix_copy[j, i] * f_vector_copy[i]
                matrix_copy[j, i:] -= matrix_copy[j, i] * matrix_copy[i, i:]

        roots = np.array([f_vector_copy[-1]])

        for i in range(order - 2, -1, -1):
            roots = np.insert(roots, 0, f_vector_copy[i] -
                              np.sum(roots * matrix_copy[i, i + 1:]))

        return roots

    @staticmethod
    def get_determinant(matrix: np.ndarray):
        matrix_copy = matrix.copy()

        for i in range(matrix_copy.shape[0]):
            for j in range(i + 1, matrix_copy.shape[0]):
                matrix_copy[j, i:] -= matrix_copy[j, i] / matrix_copy[i, i] \
                                      * matrix_copy[i, i:]

        return np.prod(matrix_copy.diagonal())

    @staticmethod
    def get_reversed_matrix(matrix: np.ndarray):
        order = matrix.shape[0]
        matrix_extended = np.hstack([matrix, np.eye(order)])

        for i in range(order):
            matrix_extended[i] /= matrix_extended[i, i]

            for j in range(i):
                matrix_extended[j, i:] -= matrix_extended[j, i] * matrix_extended[i, i:]

            for j in range(i + 1, order):
                matrix_extended[j, i:] -= matrix_extended[j, i] * matrix_extended[i, i:]

        return np.hsplit(matrix_extended, 2)[-1]

