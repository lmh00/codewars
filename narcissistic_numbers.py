# Narcissistic Numbers

def is_narcissistic(i):
    num = 0

    for n in str(i):
        num += int(n)**len(str(i))

    if i == int(num):
        return True
    else:
        return False



is_narcissistic(1634)
