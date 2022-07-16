def romanToInt(s):
    tot = 0
    add = {
        'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1
    }

    for i, n in enumerate(s):
        if i < len(s) - 1 and add[n] < add[s[i + 1]]:
            tot -= add[n]
        else:
            tot += add[n]

    return tot

romanToInt('MCMXCIV')
