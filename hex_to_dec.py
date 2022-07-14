def hex_to_dec(s):
    arr = []

    for i in s:
        if s in '0123456789':
            arr.append(int(i))
        else:
            arr.append(s)

    arr = ''.join(arr)

    print(arr)

hex_to_dec('10')
