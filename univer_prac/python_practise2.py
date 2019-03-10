a = [10, 34, 21, 11, 5, 1]
for i in range(len(a)):
    if a[i] % 2 and a[i] >= 10:
        a[i] = int(a[i] / 10)
    elif a[i] % 2:
        a[i] = -1
    else:
        st1 = str(a[i])
        st2 = ''
        for j in st1:
            st2 += j * 2
        a[i] = int(st2)
print(a)