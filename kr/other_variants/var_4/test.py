vowels = 'aeiouy'


def take_sum(string):
    sum_ = 0
    for c in string:
        sum_ += ord(c) - 96
    return sum_


def longest_streak(string):
    j, i, max_ = 0, 0, 0
    length = len(string)
    while i < length:
        while j < length and string[j] in vowels:
            j += 1
        i = j
        while i < length and string[i] not in vowels:
            i += 1
        max_ = max(take_sum(string[j:i]), max_)
        j = i
    return max_


with open('input.txt', 'r', encoding='utf-8') as open_file:
    words_dict = {word:longest_streak(word) for word in open_file.read().split()}
    for word in sorted(words_dict):
        print(word, words_dict[word], sep=' - ')
