def movie(card, ticket, perc):
    movies = 0
    non_card_sum = 0
    card_sum = card
    rounded = round(card_sum)
    discount = ticket * perc

    for i in range(card):
        if non_card_sum < rounded:
            movies += 1
            non_card_sum += ticket
            card_sum += discount
            discount *= perc
            rounded = round(card_sum)

    print(card_sum)
    print(rounded)
    print(movies)



movie(500, 15, .9)
