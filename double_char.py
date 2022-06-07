def double_char(s):
    x = []
    for i in s:
        x.append(i*2)
    y = ''.join(x)
    return y

double_char("String") # "SSttrriinngg"
double_char("Hello World") #"HHeelllloo  WWoorrlldd"
double_char("1234!_ ") # "11223344!!__  "
