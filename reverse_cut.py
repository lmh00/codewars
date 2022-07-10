def arrange(s):
    t = []

    try:
        while s:
            t.append(s[0])
            t.append(s[-1])
            s.reverse()
            s.pop(0)
            s.pop(-1)
    except:
        break

    print(t)


arrange([1, 2])
