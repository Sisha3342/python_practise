import numpy as np
from collections import namedtuple


class DanilevskyMethod:
    @staticmethod
    def get_similarity_conversion(matrix: np.ndarray, order: int):
        m_matrix = np.eye(matrix.shape[0], dtype=float)
        m_matrix[order-2, :] = -matrix[order-1, :] / matrix[order-1, order-2]
        m_matrix[order-2, order-2] /= -matrix[order-1, order-2]

        m_matrix_reversed = np.eye(matrix.shape[0], dtype=float)
        m_matrix_reversed[order-2, :] = matrix[order-1]

        conversion = namedtuple("conversion", 'm_matrix reversed_m_matrix')

        return conversion(m_matrix, m_matrix_reversed)

    @staticmethod
    def get_frobenius_and_conversion(matrix: np.ndarray):
        matrix_a = matrix.copy()

        matrix_s = np.eye(matrix.shape[0])

        for i in range(matrix.shape[0], 1, -1):
            conversion = DanilevskyMethod.get_similarity_conversion(matrix_a, i)
            matrix_s = np.matmul(matrix_s, conversion.m_matrix)
            matrix_a = np.matmul(np.matmul(conversion.reversed_m_matrix, matrix_a),
                                 conversion.m_matrix)

        frob_and_conv = namedtuple("frobenius_and_conversion", "frobenius_matrix conversion_matrix")

        return frob_and_conv(matrix_a, matrix_s)

    @staticmethod
    def get_eigenvalues(frobenius_matrix: np.ndarray):
        pass

    @staticmethod
    def get_eigenvectors(frobenius_matrix: np.ndarray, eigenvalues: np.ndarray):
        pass
