def min_sum(arr):
    arr1 = list(arr)
    arr2 = []

    for i in arr:
        arr1.pop(0)
        for j in arr1:
            arr2.append([(i*j), i, j])

    arr3 = list(arr2)
    arr4 = []

    for i in arr2:
        for j in arr3:
            arr4.append([(i[0] + j[0]), i[1], i[2], j[1], j[2]])

    print(arr)
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)

    arr5 = list(arr4)
    arr6 = []

    for i in arr4:
        if i[1] == i[2]:
            arr5.remove(i)
        elif i[1] == i[3]:
            arr5.remove(i)
        elif i[1] == i[4]:
            arr5.remove(i)
        elif i[2] == i[3]:
            arr5.remove(i)
        elif i[2] == i[4]:
            arr5.remove(i)
        elif i[3] == i[4]:
            arr5.remove(i)

    arr5.sort()

#    return arr5[0][0]

min_sum([5, 4, 2, 3, 1])
