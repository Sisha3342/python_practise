import seaborn as sns
from collections import Counter

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
