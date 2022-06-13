def robber_encode(sentence):
    s = list(sentence.lower())

    for i, v in enumerate(s):
        if v in "bcdfghjklmnpqrstvwxz":
            v = 1
            print(v)
            print(s)

robber_encode("hello world") # "hohelollolo wowororloldod"
# robber_encode("coding is fun") # "cocododinongog isos fofunon"
# robber_encode("follow the white rabbit") # "fofolollolowow tothohe wowhohitote rorabobbobitot"
# robber_encode("S.O.S") # "SOS.O.SOS"
