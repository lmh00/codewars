def compare_versions(version1,version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    tof = True
    maj = False
    min = False

    if len(v1) != len(v2):
        diff = abs(len(v1) - len(v2))

        for i in range(diff):
            if len(v1) > len(v2):
                v2.append('0')
            else:
                v1.append('0')

    for i, n in enumerate(v1):
        if int(v2[i]) > int(n) and maj == False and min == False:
            tof = False
            break
        if int(v2[i]) < int(n) and i == 0:
            maj = True
        if int(v2[i]) < int(n) and i > 0:
            min = True

    return tof

compare_versions('11.4.9', '11.4')
