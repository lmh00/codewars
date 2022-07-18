def gps(s, x):
    arr = []

    for i in range(1, len(x)):
        arr.append(x[i] - x[i - 1])
        arr[-1] = (60 / s) * 60 * arr[-1]

    if x <= 1:
        print(0)
    else:
        print(max(arr))

gps(15, [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25])
