import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dataset = pd.read_csv('https://raw.githubusercontent.com/'
                          'Sisha3342/pydata-book/2nd-edition/'
                          'datasets/babynames/yob1880.txt',
                          header=None,
                          names=['name', 'gender', 'number'])

    males_count = np.sum(dataset['gender'] == 'M')
    females_count = dataset['gender'].size - males_count

    genders = ['female', 'male']
    sizes = [females_count, males_count]
    colors = ['lightcoral', 'lightskyblue']
    plt.pie(sizes, labels=genders,
            colors=colors, autopct='%1.1f%%',
            startangle=90)
    plt.axis('equal')
    plt.savefig('pie.png')
    plt.show()
