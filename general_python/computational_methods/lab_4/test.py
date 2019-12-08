import numpy as np
from danilevsky_metod import DanilevskyMethod as DM

if __name__ == "__main__":
    test_matrix = np.array([[8.30, 3.82, 4.10, 1.90],
                            [3.92, 8.45, 6.58, 2.46],
                            [3.77, 8.41, 8.04, 2.28],
                            [2.21, 2.45, 1.69, 6.99]])

    tup = DM.get_frobenius_and_conversion(test_matrix)
    print(tup.conversion_matrix)

