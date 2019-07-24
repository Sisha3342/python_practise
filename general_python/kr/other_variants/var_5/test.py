information = open('input.txt', 'r').readline().split()
numbers, equals_to = information[0].rstrip(), int(information[1])


def change_signs(calculation):
    new_str = ''
    for c in calculation:
        if c == '-':
            new_str += '+'
        elif c == '+':
            new_str += '-'
        else:
            new_str += c
    return new_str


def take_combinations(numbers, final):
    if numbers == str(final):
        yield numbers
    else:
        start_value = 0
        for i in range(len(numbers)):
            initial = start_value * 10 + int(numbers[i])
            pos_format = take_combinations(numbers[i + 1:], final - initial)
            neg_format = take_combinations(numbers[i + 1:], initial - final)
            if pos_format is not None:
                for i in pos_format:
                    yield str(initial) + '+' + i
            if neg_format is not None:
                for i in neg_format:
                    yield str(initial) + '-' + change_signs(i)
            start_value = initial


for i in take_combinations(numbers, equals_to):
    print(i)
