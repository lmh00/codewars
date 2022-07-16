def is_opposite(s1,s2):
    tof = True
    for i, n in enumerate(s1):
        if n == n.lower() and s2[i] == n.upper() or n == n.upper() and s2[i] == n.lower():
            tof = False
            break
    return tof


is_opposite('AB', 'AB')
