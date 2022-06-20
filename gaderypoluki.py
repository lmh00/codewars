def encode(message):
    arr = []
    code = {
            'g' : 'a',
            'a' : 'g',
            'd' : 'e',
            'e' : 'd',
            'r' : 'y',
            'y' : 'r',
            'p' : 'o',
            'o' : 'p',
            'l' : 'u',
            'u' : 'l',
            'k' : 'i',
            'i' : 'k',
            'G' : 'A',
            'A' : 'G',
            'D' : 'E',
            'E' : 'D',
            'R' : 'Y',
            'Y' : 'R',
            'P' : 'O',
            'O' : 'P',
            'L' : 'U',
            'U' : 'L',
            'K' : 'I',
            'I' : 'K'
    }

    for i in list(message):
        if i in code:
            arr.append(code[i])
        else:
            arr.append(i)

    joined = "".join(arr)

    return joined

def decode(message):
        arr = []
        code = {
                'g' : 'a',
                'a' : 'g',
                'd' : 'e',
                'e' : 'd',
                'r' : 'y',
                'y' : 'r',
                'p' : 'o',
                'o' : 'p',
                'l' : 'u',
                'u' : 'l',
                'k' : 'i',
                'i' : 'k',
                'G' : 'A',
                'A' : 'G',
                'D' : 'E',
                'E' : 'D',
                'R' : 'Y',
                'Y' : 'R',
                'P' : 'O',
                'O' : 'P',
                'L' : 'U',
                'U' : 'L',
                'K' : 'I',
                'I' : 'K'
        }

        for i in list(message):
            if i in code:
                arr.append(code[i])
            else:
                arr.append(i)

        joined = "".join(arr)

        return joined


encode("ABCD")          # GBCE
encode("Ala has a cat") # Gug hgs g cgt
encode("gaderypoluki") # agedyropulik
decode("Gug hgs g cgt") # Ala has a cat
decode("agedyropulik")  # gaderypoluki
decode("GBCE")          # ABCD
