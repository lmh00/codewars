def ideal_trader(prices):
    pMax = prices[-1]
    last = 0
    totD = 1

    for i in range(len(prices) - 1, -1, -1):
        if i == 0 and prices[i] <= pMax:
            totD *= pMax / prices[i]
            break
        if prices[i] > pMax:
            totD *= pMax / last
            pMax = prices[i]
        else:
            last = prices[i]

    return totD


ideal_trader([1.0, 1.0, 1.2, 0.8, 0.9, 1.0]) # 1
