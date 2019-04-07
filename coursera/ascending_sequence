def is_ascending(a):
    i = len(a) - 1
    ascend = True
    while i and ascend:
        ascend = a[i] > a[i - 1]
        i -= 1
    return ascend


numList = list(map(int, input().split()))
if is_ascending(numList):
    print("YES")
else:
    print("NO")
