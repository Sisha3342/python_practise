import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    forms_stats = {i: 0 for i in range(1, 12)}
    scores_stats = {i: 0 for i in range(0, 101)}
    forms_scores_stats = {i: [] for i in range(1, 12)}

    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            splitted = line.split()
            forms_stats[int(splitted[-2])] += 1
            scores_stats[int(splitted[-1])] += 1
            forms_scores_stats[int(splitted[-2])].append(int(splitted[-1]))

    fig, (forms_count, scores_count, forms_scores) = plt.subplots(
        nrows=1, ncols=3,
        figsize=(10, 4)
    )

    forms_count.bar(forms_stats.keys(), forms_stats.values())
    forms_count.set_title('forms count stats')
    forms_count.set_xlabel('form')
    forms_count.set_ylabel('count')

    scores_count.bar(scores_stats.keys(), scores_stats.values())
    scores_count.set_title('scores count stats')
    scores_count.set_xlabel('score')
    scores_count.set_ylabel('count')

    mean_scores = [np.mean(scores) for scores in forms_scores_stats.values()]
    forms_scores.bar(forms_scores_stats.keys(), mean_scores)
    forms_scores.set_title('forms scores stats')
    forms_scores.set_xlabel('form')
    forms_scores.set_ylabel('mean score')

    plt.savefig('statistics.png')

    plt.show()
