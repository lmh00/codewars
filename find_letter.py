def find_missing_letter(chars):
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ch = chars

    for i in range(len(ch)):
        string = ''.join(ch)
        if string in abc:
            ans = abc.find(string) + len(string)
            return abc[ans]
            break
        else:
            ch.pop()

find_missing_letter(['n', 'o', 'q'])
