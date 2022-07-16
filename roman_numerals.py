def romanToInt(s):
    s_set = set(s)
    arr = [['IV', 4], ['IX', 9], ['XL', 40], ['XC', 90], ['CD', 400],
        ['CM', 900], ['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100],
        ['D', 500], ['M', 1000]]
    tot = 0

    for i in len(arr):
        x = s_set
        for j, n in enumerate(x):
            # if i[0] == j or i[0] == str(j + x[j+1]
            print(j, n)

romanToInt('VII')
