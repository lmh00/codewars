def reduce_fraction(fraction):
    lcd = []
    m = max(fraction[0], fraction[1])
    n = fraction[0]
    d = fraction[1]

    for i in range(1, m):
        if n % i == 0 and d % i == 0:
            lcd.append(i)

    n = n // lcd[-1]
    d = d // lcd[-1]

    if fraction[0] == 1 and fraction[1] == 1:
        return (1, 1)

    return (n, d)

reduce_fraction([20, 25])
