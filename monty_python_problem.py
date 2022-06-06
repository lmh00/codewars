def monty_hall(c, p):
    a = 0

    for i in p:
        if i != c:
            a += 1
        else:
            pass

    return int((a / len(p))*100)) + ((a / len(p))*100) > 0)



monty_hall(1, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]) # 71
monty_hall(2, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]) # 64
monty_hall(3, [3,3,2,3,3,2,2,3,2,2,1,1,1,1]) # 64
