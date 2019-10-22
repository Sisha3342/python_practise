import numpy as np


class SingleDivision:

    @staticmethod
    def __apply_straight_way(matrix: np.ndarray, f_vector: np.ndarray):
        extended_matrix = np.hstack((matrix, f_vector))
        order = extended_matrix.shape[0]

        for i in range(order):
            extended_matrix[i] /= extended_matrix[i, i]

            for j in range(i + 1, order):
                extended_matrix[j, i:] -= extended_matrix[j, i] * extended_matrix[i, i:]

        return extended_matrix

    @staticmethod
    def __apply_reversed_way(matrix: np.ndarray, f_vector: np.ndarray):
        roots = np.array([])
        order = matrix.shape[0]

        for i in range(order - 1, -1, -1):
            roots = np.insert(roots, 0, f_vector[i] -
                              np.sum(roots * matrix[i, i + 1:]))

        return roots

    @staticmethod
    def get_equation_solution(matrix: np.ndarray, f_vector: np.ndarray):
        extended_matrix = SingleDivision.__apply_straight_way(matrix, f_vector)

        return SingleDivision.__apply_reversed_way(extended_matrix[:, :-1],
                                                   extended_matrix[:, -1])

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
        extended_matrix = SingleDivision.__apply_straight_way(matrix, np.eye(order))

        # reversed way
        reversed_ = np.empty((order, order), np.float)

        for i in range(order):
            reversed_[:, i] = SingleDivision.__apply_reversed_way(extended_matrix[:, :order],
                                                                  extended_matrix[:, order+i])

        return reversed_

