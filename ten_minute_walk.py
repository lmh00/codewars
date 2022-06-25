def is_valid_walk(walk):
    total, n, s, e, w = 0, 0, 0, 0, 0

    for i in walk:
        total += 1

        if i == 'n':
            n += 1
        elif i == 's':
            s += 1
        elif i == 'e':
            e += 1
        elif i == 'w':
            w += 1

    if total < 11 and n == s and e == w:
        print(True)
    else:
        print(False)

is_valid_walk(['e', 'e', 'e', 's', 'w', 'w', 'w', 'n'])
