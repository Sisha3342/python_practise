import numpy as np


def get_matrix_norm(matrix: np.ndarray):
    return np.max(np.sum(np.abs(matrix), axis=1))
    # max sum_by_rows


def get_vector_norm(vector: np.ndarray):
    return np.max(np.abs(vector))
    # max element's module
