"""
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
"""

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(p1, p2, first):
    o = []

    if first in p1.name:
        o.append(p1)
        o.append(p2)
    else:
        o.append(p2)
        o.append(p1)

    while o[0].health >= 0:
        o[1].health -= o[0].damage_per_attack
        if o[1].health <= 0:
            return o[0].name
        o.append(o[0])
        o.pop(0)

declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew")
