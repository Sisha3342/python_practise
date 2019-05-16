def take_simple_divisors(number):
    divisors = []
    while number > 1:
        i = 2
        while number % i != 0:
            i += 1
        divisors.append(i)
        number //= i
    return divisors


def make_short_format(number_, divisors):
    formatted = str(number_) + " = "
    temp = divisors[0]
    count = 0
    for divisor in divisors:
        if divisor == temp:
            count += 1
        else:
            if count != 1:
                formatted += str(temp) + " ^ " + str(count) + " * "
            else:
                formatted += str(temp) + " * "
            temp = divisor
            count = 1
    if count != 1:
        formatted += str(temp) + " ^ " + str(count)
    else:
        formatted += str(temp)
    return formatted


numbers = set()
open_file = open('input.txt', 'r', encoding='utf-8')
for line in open_file:
    numbers |= set(map(int, line.split()))
open_file.close()
for number in sorted(numbers):
    print(make_short_format(number, take_simple_divisors(number)))
