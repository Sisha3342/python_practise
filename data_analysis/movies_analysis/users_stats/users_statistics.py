from movies_dataframes import users_df
import matplotlib.pyplot as plt

if __name__ == "__main__":
    occupations_freq = users_df.groupby('Occupation').size()
    genders_freq = users_df.groupby('Gender').size()
    ages_freq = users_df.groupby('Age').size()
    ages_freq = ages_freq[-1:].append(ages_freq[:-1])

    fig, axs = plt.subplots(2, 1, figsize=(5, 10))

    axs[0].pie(genders_freq.values, labels=genders_freq.index,
               colors=['lightcoral', 'lightskyblue'], autopct='%1.1f%%')
    axs[0].set_title('users gender relation')

    ages_freq.plot.bar(ax=axs[1])
    axs[1].set_title('users age relation')
    axs[1].set_ylabel('users count')

    plt.savefig('users_stats_1.png')
    plt.close()

    occupations_freq.plot.barh(figsize=(15, 10))
    plt.title('users occupation relation')
    plt.xlabel('users count')

    plt.savefig('users_stats_2.png')
