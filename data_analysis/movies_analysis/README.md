# Task
- [x] Read files from https://github.com/Sisha3342/pydata-book/tree/2nd-edition/datasets/movielens 
(**movies_dataframes.py**)

- [x] Analyze movies/users files separately
    - [x] movies file (**movies_stats** folder)
        - [x] display the amount of films yearly
        - [x] display the most popular genres
    - [x] users file (**users_stats** folder)
		- [x] display genders relation
		- [x] display occupations relation
		- [x] display ages relation
- [x] Analyze movies/ratings files together (**movies_extended** folder)
    - [x] Create a **movies_extended.csv** file (based on movies_df) with the amount of reviews and *min/average/max* ratings of each film
- [x] Analyze users/ratings files together (**users_extended** folder)
    - [x] Create a **users_extended.csv** file (based on users_df) each user's amount of reviews, *min/average/max* rating
 - [x] Analyze movies_df, users_df and ratings_df together (**users_favourites** folder)
    - [x] find each user's favourite (not favourite) films (user's review with the highest rating)
    - [x] find each users favourite genres (based on amount of reviews on each genre)
    - [x] save to users_favourites.csv file