import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import GridSearchCV

if __name__ == "__main__":

    titanic = pd.read_csv('titanic.csv')

    x = titanic.drop('survived', axis=1)
    y = titanic['survived']
    model = SVC()

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

    grid_params = {'C': [13, 14, 15, 16, 17],
                   'gamma': [0.0005, 0.001, 0.0015]}
    grid = GridSearchCV(model, grid_params, cv=5)
    grid.fit(x_train, y_train)
    print(grid.best_params_)

    model = grid.best_estimator_
    predicted = model.predict(x_test)
    print(accuracy_score(y_test, predicted))

    # plotting graphs for seeing gamma/accuracy relation
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    gamma_string_values = ['auto', 'scale']
    train_score_1, test_score_1 = validation_curve(model, x, y, 'gamma',
                                                   gamma_string_values, cv=5)
    gamma_float_values = np.linspace(0.001, 0.1, 20)
    train_score_2, test_score_2 = validation_curve(model, x, y, 'gamma',
                                                   gamma_float_values, cv=5)

    axes[0].bar([1, 2], train_score_1.mean(axis=1), 0.3,
                color='blue', label='train')
    axes[0].bar([1.3, 2.3], test_score_1.mean(axis=1), 0.3,
                color='red', label='test')
    axes[0].set_xticks([1.15, 2.15])
    axes[0].set_xticklabels(gamma_string_values)
    axes[0].set_xlabel('gamma value')
    axes[0].set_ylabel('model accuracy')
    axes[0].legend(loc='best')

    axes[1].plot(gamma_float_values, train_score_2.mean(axis=1),
                 color='blue', label='train')
    axes[1].plot(gamma_float_values, test_score_2.mean(axis=1),
                 color='red', label='test')
    axes[1].set_xlabel('gamma')
    axes[1].set_ylabel('model accuracy')
    axes[1].legend(loc='best')

    plt.show()
