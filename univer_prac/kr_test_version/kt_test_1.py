def string_value(string: str):
    value = 0
    for c in string:
        if c.isdigit():
            value += int(c)
        elif c.isalpha():
            value += ord(c.lower()) - 96
        else:
            value += 1
    return value


open_file = open('input_txt_1.txt', "r", encoding='utf-8')
str_list = [string.rstrip('\n') for string in open_file if string != '\n']
str_list_with_value = list(map(lambda s: (s, string_value(s)), str_list))
open_file.close()
for string in sorted(str_list_with_value, key=lambda s: s[1], reverse=True):
    print('"' + string[0] + '" =', string[1])
