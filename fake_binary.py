def fake_bin(x):
    x = [int(c) for c in str(x)]
    y = []

    for i in x:
        if i > 4:
            y.append(str(1))
        else:
            y.append(str(0))

    return ''.join(y)

fake_bin(257)
