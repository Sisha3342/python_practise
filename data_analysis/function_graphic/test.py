import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(0, 5)
    y = np.linspace(0, 5)[:, np.newaxis]
    z = x ** 2 + y ** 2

    plt.title('f(x, y) = x^2 + y^2')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
    plt.colorbar()
    plt.savefig('function graphic.png')
    plt.show()
