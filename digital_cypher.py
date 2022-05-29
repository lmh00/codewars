def encode(message, key):
    message = list(message)
    abc = list("abcdefghijklmnopqrstuvwxyz")
    key = [int(i, base=16) for i in list(str(key)*26)]
    asn = []
    out = []

    for i in message:
        if i in abc:
            asn.append(abc.index(i))

    for i in asn:
        out.append(i + key[i])

    print(message)
    print(abc)
    print(key)
    print(asn)
    print(out)

encode("scout", 1939)
