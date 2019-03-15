def tribon_list(n):
    a, b, c = 0, 0, 1
    for i in range(n):
        yield a
        a, b, c = b, c, a + b + c
num = int(input("Input num: "))
list1 = tribon_list(num)
#print(list1) ???
for i in list1:
    print(i)
