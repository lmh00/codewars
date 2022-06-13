def knight_vs_king (n, k):
    col = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8
                }

    for i in col:
        if i == n[1]:
            n[1] = col[i]

    for i in col:
        if i == k[1]:
            k[1] = col[i]

    if (k[0] - n[0]) + (k[0] - n[1]) + (k[1] - n[0]) + (k[1] - n[0]) == 5:
        print("Knight")
    elif (k[0] - n[0]) + (k[0] - n[1]) + (k[1] - n[0]) + (k[1] - n[0]) == -5:
        print("King")
    else:
        print("None")



    print("king: ", k[0], k[1])
    print("knight: ", n[0], n[1])
    print("k[0] - n[0]: ", k[0] - n[0])
    print("k[0] - n[1]: ", k[0] - n[1])
    print("k[1] - n[0]: ", k[1] - n[0])
    print("k[1] - n[1]: ", k[1] - n[1])

knight_vs_king([4, "C"], [6, "D"]) # "Knight"
knight_vs_king([7, "B"], [6, "C"]) # "King"
knight_vs_king([2, "F"], [6, "B"]) # "None"
