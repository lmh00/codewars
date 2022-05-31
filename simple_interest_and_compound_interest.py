import math

def interest(p, r, n):
    simple = p + (p * r * n)
    compound = p

    while n > 0:
        compound += compound * r
        n -= 1

    return [math.ceil(simple), math.ceil(compound)]

interest(100, 0.1, 1)
interest(100, 0.1, 2)
interest(100, 0.1, 10)
