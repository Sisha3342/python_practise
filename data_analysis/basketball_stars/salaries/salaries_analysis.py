import pandas as pd
import matplotlib.pyplot as plt


def formatter(tick, tick_number):
    return tick / 1e8


if __name__ == "__main__":
    salaries = pd.read_csv('salaries.csv')
    salaries.Salary = salaries.Salary.str.lstrip('$').astype('int64')
    fig, ax = plt.subplots(3, 1, figsize=(10, 10))

    max_avg_salaries = salaries.groupby('Player').Salary.aggregate(['sum', 'mean'])
    max_avg_salaries.plot.bar(ax=ax[0])
    ax[0].yaxis.set_major_formatter(plt.FuncFormatter(formatter))
    ax[0].set_ylabel('salary, $10^8$ dollars')
    ax[0].xaxis.set_tick_params(rotation=0)
    ax[0].set_title('max and average salaries')

    # plt.setp(plt.gca().xaxis, rotation=90)
    # print(plt.getp(plt.gca().yaxis)) 8 zeros

    plt.show()
