def divisors(n):
    arr = []

    for i in range(1, n):
        if (n % i) == 0:
            arr.append(i)

    return len(arr) + 1

divisors(100)
divisors(13)
divisors(474747)
