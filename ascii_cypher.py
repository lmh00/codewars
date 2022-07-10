def calc(x):
    arr = []
    s1 = 0
    s2 = 0

    for i in x:
        arr.append(str(ord(i)))

    total1 = ''.join(arr)

    for i in total1:
        s1 += int(i)
        if i == str(7):
            s2 += 1
        else:
            s2 += int(i)

    s3 = s1 - s2

    print(s3)


calc('abcdef')
