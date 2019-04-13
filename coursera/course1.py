class Contestant:
    surname = ''
    name = ''
    rating = 0

    def __init__(self, sur, n, rat):
        self.name = n
        self.surname = sur
        self.rating = rat


inp_file = open('input.txt', 'r', encoding='utf8')
contestants_list = []
for i in inp_file:
    info = i.split()
    contestants_list.append(Contestant(info[0], info[1], info[3]))
contestants_list.sort(key=lambda cont: cont.surname)

out_file = open('output.txt', 'w', encoding='utf8')

for i in contestants_list:
    print(i.surname, i.name, i.rating, file=out_file)
inp_file.close()
