from movies_dataframes import movies_df, ratings_df

if __name__ == "__main__":
    movies_ratings_df = ratings_df.groupby('MovieID').Rating.aggregate(
        ['size', 'min', 'mean', 'max'])
    movies_ratings_df.columns = ['reviews', 'min_rating', 'avr_rating', 'max_rating']
    movies_extended_df = movies_df.merge(movies_ratings_df, how='outer',
                                         left_index=True, right_index=True)
    movies_extended_df.eval('reviews = reviews.fillna(0)', inplace=True)

    movies_extended_df.to_csv('movies_extended.csv')
