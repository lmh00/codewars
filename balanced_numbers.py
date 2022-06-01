def balanced_num(number):
    even_list =
    even_length = 0
    even_sum_left = 0
    even_sum_right = 0

    if len(str(number)) % 2 > 0:
        if len(str(number)) == 1:
            print(f"n = {number}, balanced")
        else:
            even_length = int(len(str(number)) / 2)
            for i in range(0, even_length):
                even_sum_left += i
            print("even_list: ", even_list)
            print("even_length: ", even_length)
            print("even_sum_left: ", even_sum_left)
            print("even_sum_right: ", even_sum_right)
    else:
        print(f"n = {number}, odd")

balanced_num(1)
balanced_num(22)
balanced_num(333)
balanced_num(4444)
balanced_num(55555)
