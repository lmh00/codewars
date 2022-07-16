def permuts(n):
    x = [1,2]
    for i in range(n):
        x.append(x[-1]+x[-2])
    print(x)
    print(x[n-1])

permuts(5)
