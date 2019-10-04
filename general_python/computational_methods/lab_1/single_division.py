import numpy as np


class SingleDivision:

    @staticmethod
    def get_equation_solution(matrix: np.ndarray, f_vector: np.ndarray):
        matrix_copy = matrix.copy()
        f_vector_copy = f_vector.copy()
        order = matrix_copy.shape[0]

        # straight way
        for i in range(order):
            f_vector_copy[i] /= matrix_copy[i, i]
            matrix_copy[i] /= matrix_copy[i, i]

            for j in range(i + 1, order):
                f_vector_copy[j] -= matrix_copy[j, i] * f_vector_copy[i]
                matrix_copy[j, i:] -= matrix_copy[j, i] * matrix_copy[i, i:]

        # reversed way
        roots = np.array([f_vector_copy[-1]])

        for i in range(order - 2, -1, -1):
            roots = np.insert(roots, 0, f_vector_copy[i] -
                              np.sum(roots * matrix_copy[i, i + 1:]))

        return roots

    @staticmethod
    def get_determinant(matrix: np.ndarray):
        matrix_copy = matrix.copy()
        order = matrix.shape[0]
        leading_elements = []

        for i in range(order):
            leading_elements.append(matrix_copy[i, i])
            matrix_copy[i] /= matrix_copy[i, i]

            for j in range(i + 1, order):
                matrix_copy[j, i:] -= matrix_copy[j, i] * matrix_copy[i, i:]

        return np.prod(leading_elements)

    @staticmethod
    def get_reversed_matrix(matrix: np.ndarray):
        order = matrix.shape[0]
        matrix_extended = np.hstack([matrix, np.eye(order)])

        # straight way
        for i in range(order):
            matrix_extended[i] /= matrix_extended[i, i]

            for j in range(i + 1, order):
                matrix_extended[j, i:] -= matrix_extended[j, i] * matrix_extended[i, i:]

        # reversed way
        reversed_ = np.array(matrix_extended[-1, order:])

        for i in range(order - 2, -1, -1):
            reversed_ = np.vstack((matrix_extended[i, order:] -
                                   np.sum(matrix_extended[i, i+1:order][:, np.newaxis] *
                                          reversed_, axis=0), reversed_))

        return reversed_

