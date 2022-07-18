def is_twinprime(n):
    base = True
    base_plus = True
    base_min = True

    for i in range(n + 2):
        if i == 0 or i == 1:
            continue
        if n % i == 0 and i < n:
            base = False
        if (n + 2) % i == 0:
            base_plus = False
        if (n - 2) % i == 0 and i < (n - 2):
            base_min = False

    if base == True and base_plus == True or base == True and base_min == True:
        return True
    else:
        return False

is_twinprime(25)
