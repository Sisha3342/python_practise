import pandas as pd
from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score

if __name__ == "__main__":

    titanic = pd.read_csv('titanic.csv')

    x = titanic.drop('survived', axis=1)
    y = titanic['survived']

    model = GaussianNB()

    print(cross_val_score(model, x, y, cv=5))
