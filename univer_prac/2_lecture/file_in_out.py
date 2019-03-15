from python_practise5 import tribon_list

from_file = open(input(), "r")

num = int(from_file.read())
list1 = tribon_list(num)

to_file = open(input(), "w")
for i in list1:
    to_file.write(str(i) + '\n')
