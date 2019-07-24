string = input()
a = string.find("h")
test = string[::-1]
b = len(string) - 1 - test.find("h")
string = string[:a] + string[b + 1:]
print(string)
