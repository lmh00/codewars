def add10(x): return x + 10
def mul30(x): return x * 30

def chain(init_val, functions):
    for i in range(len(functions)):
        init_val = functions[i](init_val)
    print(init_val)



chain(42, []) # 42
chain(50, [mul30]) # 1500
chain(50, [mul30, add10]) # 1510
chain(50, [add10, mul30]) # 1800
