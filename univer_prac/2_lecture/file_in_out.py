from tribon_list_with_yield import tribon_list #is it correct import?

from_file = open(input(), "r")

num = int(from_file.read())
list1 = tribon_list(num)

to_file = open(input(), "w")
for i in list1:
    to_file.write(str(i) + '\n')
