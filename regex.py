def validate_pin(pin):
    a = 1

    for y in list("1234567890"):
        for x in list(pin):

    if len(pin) == 4 or len(pin) == 6:
        pass
    else:
        a -= 1

    print(a)


validate_pin("1234")
validate_pin("12345")
validate_pin("123456")
validate_pin("1234a6")
