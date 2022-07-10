def merge_arrays(arr1, arr2):
    arr3 = arr1 + arr2
    arr4 = []

    for i in arr3:
        if i not in arr4:
            arr4.append(i)

    arr4.sort()
    return arr4

merge_arrays([1,3,2],[7,5,6])
