def sum_groups(arr):
    odd = []
    even = []
    done = 0

    for i in arr:
        if i % 2: #odd
            odd.append(i)
        else: #even
            even.append(i)

    print(odd, even)


sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9])
