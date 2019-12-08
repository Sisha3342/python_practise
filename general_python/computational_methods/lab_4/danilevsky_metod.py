import numpy as np


class DanilevskyMethod:
    @staticmethod
    def __form_matrix_m(matrix: np.ndarray, order: int):
        m_matrix = np.eye(matrix.shape[0], dtype=float)

        m_matrix[order-2, :] = -matrix[order-1, :] / matrix[order-1, order-2]

        m_matrix[order-2, order-2] *= -1

        return m_matrix


    @staticmethod
    def form_frobenius_matrix(matrix: np.ndarray):
        pass

    @staticmethod
    def get_eigenvalues(frobenius_matrix: np.ndarray):
        pass

    @staticmethod
    def get_eigenvectors(frobenius_matrix: np.ndarray, eigenvalues: np.ndarray):
        pass
