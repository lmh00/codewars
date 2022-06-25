def fibonacci(n):
    a = []
    t = 0

    for i in range(n):
        if t < 2:
            a.append(t)
            t += 1
        else:
            x = a[i-1] + a[i-2]
            a.append(x)

    return a[n-1]


fibonacci(7)
