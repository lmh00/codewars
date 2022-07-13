def faro_cycles(deck_size):
    deck = []
    untouched = []
    current = []
    left_hand = []
    right_hand = []
    half = deck_size // 2
    shuffles = 0

    for i in range(deck_size):
        deck.append(i)

    current = deck

    while current != untouched:
        untouched = deck
        shuffles += 1

        left_hand = current[:half]
        right_hand = current[half:]
        current = []

        for i in range(len(left_hand)):
            current.append(left_hand[i])
            current.append(right_hand[i])

    return shuffles

faro_cycles(52)
