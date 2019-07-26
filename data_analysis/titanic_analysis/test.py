import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def make_labels(labels, sizes):
    total = sizes.sum()
    stats = '({v:d}, {p:.2f}%)'
    final_labels = [i[0].format(stats.format(v=i[1], p=100 * i[1] / total))
                    for i in zip(labels, sizes)]
    return final_labels


if __name__ == "__main__":
    destination = 'https://raw.githubusercontent.com/' \
                  'Sisha3342/pydata-book/2nd-edition/' \
                  'datasets/titanic/{}'

    survived_1 = pd.read_csv(destination.format('genderclassmodel.csv'))
    survived_2 = pd.read_csv(destination.format('gendermodel.csv'))

    finally_survived = survived_1
    finally_survived.loc[survived_1['Survived'] != survived_2['Survived'],
                         'Survived'] = np.nan

    last_passengers_info = pd.read_csv(destination.format('test.csv'))
    last_passengers_info = pd.merge(finally_survived, last_passengers_info,
                                    on='PassengerId')
    start_passengers_info = pd.read_csv(destination.format('train.csv'))

    passengers_final = pd.concat([start_passengers_info, last_passengers_info],
                                 ignore_index=True)
    passengers_final = passengers_final.set_index('PassengerId')

    fig, axs = plt.subplots()
    # first graphic
    survived_count = np.nansum(passengers_final['Survived'], dtype=np.int)
    unknown_count = passengers_final['Survived'].isnull().sum()
    dead_count = passengers_final.index.size - survived_count - unknown_count

    labels = np.array(['survived{}', 'dead{}', 'unknown{}'])
    sizes = np.array([survived_count, dead_count, unknown_count])
    patches, texts = axs.pie(sizes, colors=['green', 'red', 'grey'])
    axs.legend(patches, make_labels(labels, sizes), loc='best')
    axs.axis('equal')
    axs.set_title('death rate')
    plt.show()
