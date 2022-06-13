def solution(string, ending):
    if ending == string[(len(string)-len(ending)):]:
        print(True)
    else:
        print(False)




solution('abcde', 'cde') # True
solution('abcde', 'abc') # False
solution('abcde', '') # True
