def cipher_text(plain):
    new = str.lower(plain)
    new = ''.join(i for i in new if i.isalnum())
    sqr = round(len(new) ** (1/2)) + 1
    mix = [new[i:i + sqr] for i in range(0, len(new), sqr)]
    fin = []

    for i in range(sqr):
        for j in mix[i]:
            print(j)

cipher_text('When nobody is around, the trees gossip about the people who have walked under them.')
