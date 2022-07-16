def find_mult10_SF(n):
    arr1 = []
    arr2 = []

    for i in range(1, 7):
        arr1.append(i ** n)
        arr2.append(i ** (n + 1))

    s1n = arr1[0] + arr1[1] + arr1[2]
    s2n = arr1[0] + arr1[1] + arr1[3]
    s3n = sum(arr1)
    stn = s3n - s2n - s1n
    s1np1 = arr2[0] + arr2[1] + arr2[2]
    s2np1 = arr2[0] + arr2[1] + arr2[3]
    s3np1 = sum(arr2)
    stnp1 = s3np1 - s2np1 - s1np1
    sfn = (stnp1 - (5 * stn) - 4) / 4

    print('arr1 = ', arr1)
    print('arr2 = ', arr2)
    print('s1n = ', s1n)
    print('s2n = ', s2n)
    print('s3n = ', s3n)
    print('stn = ', stn)
    print('s1np1 = ', s1np1)
    print('s2np1 = ', s2np1)
    print('s3np1 = ', s3np1)
    print('stnp1 = ', stnp1)
    print('sfn = ', sfn)


find_mult10_SF(1)
