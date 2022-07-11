def divisions(n, divisor):
    t = n
    c = 0

    while t // divisor > 1:
        t = t // divisor
        print('t = ', t)
        c += 1
        print('c = ', c)
    else:
        print(c)

divisions(100, 2)
