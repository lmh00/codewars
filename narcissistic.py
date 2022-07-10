def narcissistic(value):
    string = str(value)
    string = [ch for ch in string]
    p = len(string)
    t = 0

    for i in string:
        t += int(i) ** p

    print(t)

    if t == value or len(string) == 1:
        print(True)
    else:
        print(False)

narcissistic(1634)
