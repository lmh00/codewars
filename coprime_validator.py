def are_coprime(n, m):
    n_arr = []
    m_arr = []
    n_arr2 = []
    m_arr2 = []
    counter = 0

    for i in range(1, 100):
        n_arr.append(n / i)
        m_arr.append(m / i)

    for i in n_arr:
        if i - int(i) == 0:
            n_arr2.append(i)

    for i in m_arr:
        if i - int(i) == 0:
            m_arr2.append(i)

    for i in n_arr2:
        for j in m_arr2:
            if i == j:
                counter += 1

    if counter > 1:
        return False
    else:
        return True

are_coprime(5, 10)
