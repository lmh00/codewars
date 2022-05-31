def remove(s):

    s = s.split(" ")

    print(1, s)

    for i in s:
        if i.count("!") == 1:
            print(2, s)
            s.pop()
            print(3, s)

    s = " ".join(str(x) for x in s)
    print(4, s)

    print(5, s)

remove('Hi! Hi!')
