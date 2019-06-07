from mimesis import Person
from random import randint


if __name__ == '__main__':
    person = Person('ru')
    with open('data.txt', 'w', encoding='utf-8') as data_file:
        for _ in range(100):
            print(person.full_name(), randint(1, 11), randint(0, 100), file=data_file)
