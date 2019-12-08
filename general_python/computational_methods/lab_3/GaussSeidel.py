import numpy as np
import Norm


class GaussSeidel:
    @staticmethod
    def get_solution(sys_matrix: np.ndarray, f_vector: np.ndarray, epsilon: float):
        order = f_vector.shape[0]
        current_x = f_vector / sys_matrix.diagonal()

        def get_next_x(begin_x: np.ndarray):
            new_x = begin_x.copy()

            for i in range(order):
                new_x[i] = -np.sum(sys_matrix[i, :i] * new_x[:i] / sys_matrix[i, i]) - \
                           np.sum(sys_matrix[i, i+1:] * new_x[i+1:] / sys_matrix[i, i]) + \
                           f_vector[i] / sys_matrix[i, i]

            return new_x

        k = 0
        while np.abs(Norm.get_vector_norm(np.matmul(sys_matrix, current_x) - f_vector)) > epsilon:
            current_x = get_next_x(current_x)
            k += 1

        print(k)

        return current_x
