def rake_garden(garden):
    garden = garden.split(' ')

    for thing in garden:
        if thing == 'slug':
            thing = 'rock'
        elif thing == 'ant':
            thing = 'rock'
        elif thing == 'snail':
            thing = 'rock'
        elif thing == 'spider':
            thing = 'rock'

    print(garden)


rake_garden('gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel gravel snail rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant gravel gravel gravel gravel rock slug gravel gravel gravel gravel gravel snail gravel gravel rock gravel snail slug gravel gravel spider gravel gravel gravel gravel gravel gravel gravel gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel gravel moss gravel gravel gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider gravel rock gravel gravel')
