import seaborn as sns
import pandas as pd
from collections import Counter
from sklearn.feature_extraction import DictVectorizer

if __name__ == "__main__":
    titanic = sns.load_dataset('titanic').drop(['alive', 'embark_town',
                                                'adult_male', 'deck'],
                                               axis=1)

    embarked_mc = Counter(titanic.embarked).most_common(4)
    titanic.embarked.fillna(embarked_mc[0][0], inplace=True)

    combinations = (('male', 'man'), ('male', 'child'),
                    ('female', 'woman'), ('female', 'child'))

    masks = ((titanic.sex == combo[0]) & (titanic.who == combo[1])
             for combo in combinations)

    for mask in masks:
        titanic.loc[mask, 'age'] = titanic.loc[mask, 'age'].fillna(
            titanic.loc[mask, 'age'].mean()).astype('int')

    titanic.rename(columns={'sex': 'is_male'}, inplace=True)
    sex_dict = {'male': 1, 'female': 0}
    titanic.eval('is_male = is_male.map(@sex_dict)', inplace=True)

    vec = DictVectorizer(int, sparse=False)
    titanic = pd.DataFrame(vec.fit_transform(titanic.to_dict('records')),
                           columns=vec.get_feature_names())

    titanic.to_csv('titanic.csv')
