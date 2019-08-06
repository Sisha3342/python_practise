from movies_dataframes import movies
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    axes[0].set_ylabel('films')
    axes[0].set_title('films yearly')
    movies_yearly = movies.groupby('Year').size().plot(ax=axes[0])

    genres_list = movies.Genre.str.split('|').sum()
    axes[1].hist(genres_list, 18, facecolor='blue', alpha=0.5, rwidth=2)
    axes[1].tick_params(axis='x', labelrotation=90)
    axes[1].set_title('genres frequency')
    axes[1].set_ylabel('films')
    axes[1].set_xlabel('genre')

    plt.savefig('movies_stats.png')
    plt.show()
