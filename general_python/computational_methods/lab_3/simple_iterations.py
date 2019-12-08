import numpy as np
import Norm


class SimpleIterations:
    def __init__(self, matrix_a: np.ndarray, f_vector: np.ndarray, epsilon: np.float):
        self.sys_matrix = matrix_a
        self.f_vector = f_vector
        self.epsilon = epsilon

        self.new_sys_matrix = np.matmul(matrix_a.T, matrix_a)
        self.new_f_vector = np.matmul(matrix_a.T, f_vector)
        self.order = matrix_a.shape[0]
        self.norm = Norm.get_matrix_norm(self.new_sys_matrix)

    def get_matrix_b(self):
        return np.eye(self.order) - self.new_sys_matrix / self.norm

    def get_vector_b(self):
        return self.new_f_vector / self.norm

    def get_solution(self):
        vector_b = self.get_vector_b()
        matrix_b = self.get_matrix_b()

        print(vector_b)
        print(matrix_b)

        current_x = vector_b
        k = 0

        while np.abs(Norm.get_vector_norm(np.matmul(self.sys_matrix, current_x) - self.f_vector)) > self.epsilon:
            current_x = np.matmul(matrix_b, current_x) + vector_b
            k += 1

        print(k)

        return current_x
