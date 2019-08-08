from movies_dataframes import users_df, ratings_df

if __name__ == "__main__":
    users_reviews_df = ratings_df.groupby('UserID').Rating.aggregate(['size', 'min',
                                                                      'mean', 'max'])
    users_reviews_df.columns = ['reviews', 'min_rating', 'avr_rating', 'max_rating']
    users_extended_df = users_df.merge(users_reviews_df, 'outer', left_index=True,
                                       right_index=True)

    users_extended_df.to_csv('users_extended.csv')
