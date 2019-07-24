from mimesis import Person
from random import randint


if __name__ == '__main__':
    person = Person('ru')
    for year in range(2000, 2011):
        with open('{}_data.txt'.format(year), 'w', encoding='utf-8') as data_file:
            for _ in range(1000):
                print(person.full_name(), ',', randint(1, 11),
                      ',', randint(0, 100), sep='', file=data_file)
