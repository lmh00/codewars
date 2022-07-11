def heron(a, b, c):
    s = (a + b + c) / 2
    y = s * (s - a) * (s - b) * (s - c)
    x = round(y ** 0.5, 2)

    return x

heron(3, 4, 5)
