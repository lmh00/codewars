def solve(s):
    s2 = []
    d = 0
    n = 0

    for i in s:
        if d == 0:
            if i == '[':
                d = 1
                if s2 == []:
                    continue
                else:
                    s2.pop()
            elif i == '*':
                continue
            elif i in '0123456789':
                n = int(i) - 1
                while n > 0:
                    if s2 == []:
                        n -= 1
                    else:
                        s2.pop()
                        n -= 1
            else:
                s2.append(i)
        elif d == 1:
            if i == ']':
                d = 0
            else:
                continue

    s2 = ''.join(s2)
    print(s2)
    
solve("[backspace]buaoxiykyognc[backspace]*2psnxs siq[backspace]*2waf[backspace]*5[backspace]*3[backspace]hrc loippdcopp[backspace]*12lnqcpmi   [backspace]bcyjjllgtjfl  pqknqvp [backspace]*2 pew[backspace]*4jwm[backspace]*6 jwywhspn[backspace]dclxonlxjklwa[backspace]")
