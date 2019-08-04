import pandas

if __name__ == "__main__":
    movies = pandas.read_csv('https://raw.githubusercontent.com/Sisha3342/'
                             'pydata-book/2nd-edition/datasets/movielens/movies.dat',
                             sep='::', names=['ID', 'Name', 'Genre'], index_col='ID',
                             engine='python')
    movies['Year'] = movies.Name.str[-5:-1]
    movies.Name = movies.Name.str.replace('\(\w+\)', '', regex=True)

    users = pandas.read_csv('https://raw.githubusercontent.com/Sisha3342/'
                            'pydata-book/2nd-edition/datasets/movielens/users.dat',
                            sep='::', names=['ID', 'Gender', 'Age', 'Occupation', 'Zip'],
                            index_col='ID', engine='python')

    occupations = {0: 'other', 1: 'academic/educator', 2: 'artist',
                   3: 'clerical/admin', 4: 'college/grad student', 5: 'customer service',
                   6: 'doctor/health care', 7: 'executive/managerial', 8: 'farmer',
                   9: 'homemaker', 10: 'K-12 student', 11: 'lawyer',
                   12: 'programmer', 13: 'retired', 14: 'sales/marketing',
                   15: 'scientist', 16: 'self-employed', 17: 'technician/engineer',
                   18: 'tradesman/craftsman', 19: 'unemployed', 20: 'writer'}

    ages = {1: 'Under 18', 18: '18-24', 25: '25-34', 35: '35-44', 45: '45-49',
            50: '50-55', 56: '56+'}

    users.eval('Age = Age.apply(@ages.get)', inplace=True)
    users.eval('Occupation = Occupation.apply(@occupations.get)', inplace=True)

    ratings = pandas.read_csv('https://raw.githubusercontent.com/Sisha3342/'
                              'pydata-book/2nd-edition/datasets/movielens/ratings.dat',
                              sep='::', names=['UserID', 'MovieID', 'Rating', 'Timestamp'],
                              engine='python')
