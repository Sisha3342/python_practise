vowels = 'aeiouy'


def longest_streak(string):
    i, max_ = 0, 0
    length = len(string)
    while i < length:
        sum_ = 0
        while i < length and string[i] in vowels:
            i += 1
        while i < length and string[i] not in vowels:
            sum_ += ord(string[i]) - 96
            i += 1
        max_ = max(sum_, max_)
    return max_


with open('input.txt', 'r', encoding='utf-8') as open_file:
    words_dict = {word:longest_streak(word) for word in open_file.read().split()}
    for word in sorted(words_dict):
        print(word, words_dict[word], sep=' - ')
