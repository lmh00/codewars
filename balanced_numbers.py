def balanced_num(number):
    length = len(str(number))
    arr = []
    left = 0
    right = 0

    for i in str(number):
        arr.append(int(i))

    for i in range(length):
        if (i < length // 2):
            left += arr[i]
        else:
            right += arr[i]

    if length % 2 > 0:
        right -= arr[(length // 2)]
    else:
        left -= arr[((length // 2) - 1)]
        right -= arr[(length // 2)]


    if length < 3:
        return "Balanced"
    else:
        if left != right:
            return "Not Balanced"
        else:
            return "Balanced"

balanced_num(1)
balanced_num(22)
balanced_num(233)
balanced_num(4244)
balanced_num(52555)
