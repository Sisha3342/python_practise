from movies_dataframes import movies_df, ratings_df, users_df
import pandas as pd
import numpy as np
from collections import Counter

def find_liked_disliked(x):
    liked_films_id = x.query('Rating.max() == Rating').MovieID.to_numpy()
    disliked_films_id = x.query('Rating.min() == Rating').MovieID.to_numpy()
    return pd.Series([liked_films_id, disliked_films_id],
                     index=['liked_films', 'disliked_films'])


def match_film_name(movie_id):
    return movies_df.loc[movie_id].Name


def take_popular_genres(reviews):
    genres_list = movies_df.loc[reviews.MovieID].Genre.str.split('|').sum()
    favourite = Counter(genres_list).most_common(1)[0]
    return '{genre} ({times})'.format(genre=favourite[0], times=favourite[1])


if __name__ == "__main__":
    vectorized_match = np.vectorize(match_film_name)

    mostly_watched_genres = ratings_df.groupby('UserID').\
        apply(take_popular_genres).rename('mostly watched genre (times watched)')

    liked_disliked_id = ratings_df.groupby('UserID').\
        apply(find_liked_disliked)

    liked_disliked_films = liked_disliked_id.applymap(vectorized_match)

    users_favourites = users_df.merge(mostly_watched_genres, left_index=True,
                                      right_index=True)
    users_favourites = users_favourites.merge(liked_disliked_films, left_index=True,
                                              right_index=True)

    users_favourites.to_csv('users_favourites.csv')
