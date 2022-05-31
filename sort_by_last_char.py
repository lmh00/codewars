def last(s):
    arr1 = []
    arr2 = []
    arr3 = []

    s = s.split(" ")

    for i in s:
        arr1.append([i[-1], s.index(i)])

    arr1.sort()

    for i in arr1:
        arr2.append(i[1])

    for i in arr2:
        arr3.append(s[i])

    return arr3


last("man i need a taxi up to ubud")
