def longestCommonPrefix(strs):
    arr = []
    arr2 = ''
    is_in = True
    len = 0

    for i in strs[0]:
        arr.append(i)
        arr2 = ''.join(arr)
        len += 1

        for j in strs:
            if j.find(arr2, 0, len) == -1:
                is_in = False

        if is_in == False:
            arr2 = arr2[:-1]
            break

    return arr2

longestCommonPrefix(['flower', 'flow', 'flitter'])
