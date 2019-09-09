import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def formatter(tick, tick_number):
    return tick / 1e7


def generate_plot_values(player_df):
    teams = player_df.Team.unique()
    final_list = []
    for team in teams:
        final_list.append(player_df.Season)
        final_list.append(np.ma.masked_where(
            player_df.Team != team, player_df.Salary))
    return final_list


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
    plt.clf()

    fig, ax = plt.subplots(1, 3, figsize=(20, 10))

    groups = [salaries.groupby('Player').get_group(name)
              for name in salaries.Player.unique()]

    for i, player_group in enumerate(groups):
        ax[i].plot(*generate_plot_values(player_group))
        ax[i].yaxis.set_major_formatter(plt.FuncFormatter(formatter))
        ax[i].set_ylabel('salary, $10^7$ dollars')
        ax[i].set_xlabel('Season')
        ax[i].set_title(player_group.Player.iloc[0])
        ax[i].xaxis.set_tick_params(rotation=90)
        ax[i].legend(player_group.Team.unique(), loc='upper left')
        ax[i].set_title(player_group.Player.iloc[0])

    plt.savefig("player's_salary_changes.png")
