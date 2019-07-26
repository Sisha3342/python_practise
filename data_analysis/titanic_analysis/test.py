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

    fig, axs = plt.subplots(2)

    # first graphic
    survived_count = np.nansum(passengers_final['Survived'], dtype=np.int)
    unknown_count = passengers_final['Survived'].isnull().sum()
    dead_count = passengers_final.index.size - survived_count - unknown_count

    labels_1 = ['survived{}', 'dead{}', 'unknown{}']
    sizes_1 = np.array([survived_count, dead_count, unknown_count])
    patches_1, texts_1 = axs[0].pie(sizes_1, colors=['green', 'red', 'grey'])
    axs[0].legend(patches_1, make_labels(labels_1, sizes_1), loc='best')
    axs[0].axis('equal')
    axs[0].set_title('death rate')

    # second graphic
    males_survived = np.nansum(passengers_final.loc[passengers_final['Sex'] == 'male', 'Survived'],
                               dtype=np.int)
    females_survived = survived_count - males_survived

    labels_2 = ['males{}', 'females{}']
    sizes_2 = np.array([males_survived, females_survived])
    patches_2, texts_2 = axs[1].pie(sizes_2, colors=['lightskyblue', 'lightcoral'])
    axs[1].legend(patches_2, make_labels(labels_2, sizes_2), loc='best')
    axs[1].axis('equal')
    axs[1].set_title('survived males/females relation')
    plt.show()
