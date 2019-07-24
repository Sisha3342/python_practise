from tribon_list_with_yield import tribon_list

with open(input(), "r") as from_file:
    num = int(from_file.read())
    
list1 = tribon_list(num)

with open(input(), "w") as to_file:
    to_file.write('\n'.join(str(i) for i in list1))
