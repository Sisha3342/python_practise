import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

if __name__ == "__main__":
    mean = [0, 0]
    cov = [[1, 2],
           [2, 5]]
    x = np.random.multivariate_normal(mean, cov, 100)

    indices = np.random.choice(x.shape[0], 20, replace=False)
    area = np.full(100, rcParams['lines.markersize'] ** 2)
    area[indices] = 200
    colors = np.full(100, 'blue')
    colors[indices] = 'red'

    plt.scatter(x[:, 0], x[:, 1], alpha=0.3, s=area, c=colors)
    plt.savefig('scatter.png')
    plt.show()
