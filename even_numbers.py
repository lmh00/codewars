def even_numbers(arr,n):
    e = []

    for i in arr:
        if i % 2 == 0:
            e.append(i)

    for i in range(len(e)-n):
        e.remove(e[0])

    return e


even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) # => [4, 6, 8]
even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) # => [-8, 26]
even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) # => [6]
