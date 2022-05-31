def ghostbusters(building):
    if " " in building:
        no_ghosts = building.replace(' ', '')
        return no_ghosts
    else:
        return "You just wanted my autograph didn't you?"

ghostbusters("helloworld")
