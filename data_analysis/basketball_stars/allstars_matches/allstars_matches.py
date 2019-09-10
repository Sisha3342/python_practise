import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    allStars = pd.read_csv('allstar_games_stats.csv')
    grid = plt.GridSpec(2, 3)
    fig = plt.figure(figsize=(15, 15))
    matches_ax = fig.add_subplot(grid[0, :])
    positions_ax = [fig.add_subplot(grid[1, i]) for i in range(3)]

    with plt.style.context('seaborn-bright'):
        matches = allStars.groupby('Player').size()
        matches.plot(ax=matches_ax, kind='bar')
        matches_ax.xaxis.set_tick_params(rotation=0)
        matches_ax.set_title('All-stars matches played')
        matches_ax.set_ylabel('matches')
        players_names = matches.index

    with plt.style.context('classic'):
        positions = allStars.groupby('Player').Pos.value_counts()
        for i, name in enumerate(players_names):
            positions[name].plot(ax=positions_ax[i], kind='bar')
            positions_ax[i].set_title('{}\npositions'.format(name))
            positions_ax[i].set_ylabel('matches')
            positions_ax[i].xaxis.set_tick_params(rotation=0)
    plt.savefig('matches_and_positions.png')
