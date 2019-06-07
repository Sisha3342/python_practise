import matplotlib.mlab as ml
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    with open('data.txt', 'r', encoding='utf-8') as get_data_file:
        data = [(int(line.split()[2]), int(line.split()[3])) for line in get_data_file]
        forms_, scores_ = zip(*data)

    plt.xlabel('forms')
    plt.ylabel('count')
    plt.hist(forms_, bins=40, color='red', rwidth=1)
    plt.savefig('forms_stats.png')
    plt.close()
    plt.xlabel('scores')
    plt.hist(scores_, bins=40, rwidth=1)
    plt.savefig('scores_start.png')
