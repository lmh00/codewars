def alternate(n, first_value, second_value):
    x = n
    arr = []

    while x > 0:
        arr.append(first_value)
        x -= 1
        if x > 0:
            arr.append(second_value)
            x -= 1

    return arr

alternate(5, "true", "false")
