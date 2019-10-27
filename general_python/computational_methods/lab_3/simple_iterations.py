import numpy as np


def get_matrix_norm(matrix: np.ndarray):
    return np.max(np.sum(np.abs(matrix), axis=1))
    # max sum_by_rows


def get_vector_norm(vector: np.ndarray):
    return np.sqrt(np.sum(vector ** 2))


class SimpleIterations:

    def __init__(self, matrix_a: np.ndarray, vector_f: np.ndarray, epsilon: np.float):
        self.sys_matrix = matrix_a
        self.vector_f = vector_f
        self.epsilon = epsilon

        self.new_sys_matrix = np.matmul(matrix_a.T, matrix_a)
        self.new_vector_f = np.matmul(matrix_a.T, vector_f)
        self.order = matrix_a.shape[0]
        self.norm = get_matrix_norm(self.new_sys_matrix)

    def get_matrix_b(self):
        return np.eye(self.order) - self.new_sys_matrix / self.norm

    def get_vector_b(self):
        return self.new_vector_f / self.norm

    def get_solution(self):
        vector_b = self.get_vector_b()
        matrix_b = self.get_matrix_b()

        current_x = vector_b
        new_x = np.matmul(matrix_b, current_x) + vector_b
        k = 0

        while np.abs(get_vector_norm(new_x - current_x)) > self.epsilon:
            current_x = new_x
            new_x = np.matmul(matrix_b, current_x) + vector_b
            k += 1

        print(k)

        return new_x
