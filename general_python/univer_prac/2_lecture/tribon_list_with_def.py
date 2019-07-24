def tribon_list(n):
    a = [0, 0, 1]
    for i in range(3, n, 1):
        a.append(a[i - 3] + a[i - 2] + a[i - 1])
    return a
num = int(input("Input num: "))
b = tribon_list(num)
print(b)
