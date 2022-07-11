def pyramid_height(n):
    total = 0
    levels = 0

    for i in range(n):
        total += i ** 2
        levels += 1

        if n < total:
            levels -= 2
            break

    print(levels)

pyramid_height(30)
