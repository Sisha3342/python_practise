import numpy as np
import pandas as pd

if __name__ == '__main__':
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


