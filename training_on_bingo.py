def bingo(array):
    bingo = [2, 9, 14, 7, 15]
    yes = 0

    arr = list(dict.fromkeys(array))

    for i in arr:
        for j in bingo:
            if j in bingo:
                yes += 1

    print(arr)
    print(array)
    
    if yes == 5:
        print("WIN")
    else:
        print("LOSE")

bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
