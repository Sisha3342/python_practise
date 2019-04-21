myDict = dict()
open_file = open("input.txt", "r", encoding="utf8")
for line in open_file:
    for word in line.split():
        myDict[word] = myDict.get(word, 0) + 1
word_list = [(value, key) for key, value in myDict.items()]
word_list.sort(key=lambda x: (-x[0], x[1]))
for info in word_list:
    print(info[1])
