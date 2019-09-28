import numpy as np


class SingleDivision:

    @staticmethod
    def get_equation_solution(matrix: np.ndarray, f_vector: np.ndarray):
        pass

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
        pass
