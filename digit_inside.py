def numbers_with_digit_inside(x, d):
    arr = []
    p = 1

    for i in range(1, x + 1):
        if str(d) in str(i):
            arr.append(i)
            p *= i

    print(len(arr), sum(arr), p)

numbers_with_digit_inside(5, 6)
