def sum_two_smallest_numbers(numbers):
    arr = []

    for i in numbers:
        if i > 0:
            arr.append(i)

    arr.sort()

    return arr[0] + arr[1]

sum_two_smallest_numbers([5, 8, 12, 18, 22])
