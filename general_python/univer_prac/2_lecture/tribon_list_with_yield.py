def tribon_list(n):
    a, b, c = 0, 0, 1
    for i in range(n):
        yield a
        a, b, c = b, c, a + b + c
#print(list1 = tribon_list(n)) ???
#if __name__ == '__main__': 
