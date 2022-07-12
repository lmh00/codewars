def ascend_descend(length, min, max):
    arr = []
    cur = min
    des = False

    if max < min or length == 0:
        # return ''
        print('')

    for i in range(length):
        if min == max:
            arr.append(str(cur))
        elif des == False and cur < max:
            arr.append(str(cur))
            cur += 1
        elif des == False and cur == max:
            arr.append(str(cur))
            cur -= 1
            des = True
        elif des == True and cur > min:
            arr.append(str(cur))
            cur -= 1
        elif des == True and cur == min:
            arr.append(str(cur))
            cur += 1
            des = False

    arr = ''.join(arr)
    arr = arr[0:length]
    # return arr
    print(arr)


ascend_descend(24, 5, 5)
