def dot(n, m):
    top = '+---+'
    mid = '| o |'
    bot = '+---+'
    br = '\n'

    for i in range(1, n):
        top += '---+'
        mid += ' o |'
        bot += '---+'

    string = top + br + mid + br + bot

    for i in range(1, m):
        string += (br + mid + br + bot)

    return string

dot(5, 3)
