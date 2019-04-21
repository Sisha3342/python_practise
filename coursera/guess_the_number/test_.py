max_number = int(input())
question = input()
maybe_set = set(x for x in range(1, max_number + 1))
answer = ""

while question != "HELP":
    temp_set = set(map(int, question.split()))
    answer = input()
    if answer == "YES":
        maybe_set &= temp_set
    else:
        maybe_set -= temp_set
    question = input()

print(*sorted(maybe_set))
