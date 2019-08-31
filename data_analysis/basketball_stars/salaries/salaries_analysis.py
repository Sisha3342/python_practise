import pandas as pd
import matplotlib.pyplot as plt


def formatter(tick, tick_number):
    return tick / 1e7


if __name__ == "__main__":
    salaries = pd.read_csv('salaries.csv')
    salaries.Salary = salaries.Salary.str.lstrip('$').astype('int64')
    fig, ax = plt.subplots(2, 1, figsize=(7, 7))

    total_avg_salaries = salaries.groupby('Player').Salary.aggregate(['sum', 'mean'])
    total_avg_salaries.plot(kind='bar', ax=ax[0])
    ax[0].yaxis.set_major_formatter(plt.FuncFormatter(formatter))
    ax[0].set_ylabel('salary, $10^7$ dollars')
    ax[0].xaxis.set_tick_params(rotation=0)

    max_min_salaries = salaries.groupby('Player').Salary.aggregate(['max', 'min'])
    max_min_salaries.plot(kind='bar', ax=ax[1], sharex=ax[0])
    ax[1].yaxis.set_major_formatter(plt.FuncFormatter(formatter))
    ax[1].set_ylabel('salary, $10^7$ dollars')
    ax[1].xaxis.set_tick_params(rotation=0)

    plt.savefig('comparison_with_each_other.png')
