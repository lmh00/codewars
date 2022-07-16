def divisions(n, divisor):
    count = 0

    while n // 4:
        count += 1
        n = n // 4

    return count

divisions(16, 4)
