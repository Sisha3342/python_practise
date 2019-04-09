def merge(list1, list2):
    new_list = []
    len1 = len(list1)
    len2 = len(list2)
    i = 0
    j = 0
    while j != len2 and i != len1:
        i_elem = list1[i]
        j_elem = list2[j]

        if i_elem < j_elem:
            new_list.append(i_elem)
            i += 1
        elif i_elem > j_elem:
            new_list.append(j_elem)
            j += 1
        else:
            new_list.append(j_elem)
            new_list.append(i_elem)
            i += 1
            j += 1
    if j == len2:
        new_list += list1[i:]
    else:
        new_list += list2[j:]

    return new_list


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
