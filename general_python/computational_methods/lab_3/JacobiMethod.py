import numpy as np
import Norm


class JacobiMethod:
    @staticmethod
    def get_solution(sys_matrix: np.ndarray, f_vector: np.ndarray, epsilon: float):
        vector_b = f_vector / sys_matrix.diagonal()

        matrix_b = -sys_matrix / sys_matrix.diagonal()[:, np.newaxis]
        np.fill_diagonal(matrix_b, 0)

        matrix_b_norm = Norm.get_matrix_norm(matrix_b)

        prior = np.log(epsilon * (1 - matrix_b_norm) /
                       Norm.get_vector_norm(vector_b)) // np.log(matrix_b_norm) + 1

        current_x = vector_b
        new_x = np.matmul(matrix_b, current_x) + vector_b
        k = 0

        while Norm.get_vector_norm(new_x - current_x) > epsilon:
            current_x = new_x
            new_x = np.matmul(matrix_b, current_x) + vector_b
            k += 1

        return new_x
