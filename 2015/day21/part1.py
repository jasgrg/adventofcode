import itertools

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0
#
# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5
#
# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

weapons = [
    {'name': 'dagger', 'cost': 8, 'damage': 4, 'armor': 0},
    {'name': 'shortsword', 'cost': 10, 'damage': 5, 'armor': 0},
    {'name': 'warhammer', 'cost': 25, 'damage': 6, 'armor': 0},
    {'name': 'longsword', 'cost': 40, 'damage': 7, 'armor': 0},
    {'name': 'greataxe', 'cost': 74, 'damage': 8, 'armor': 0}
]
armors = [
    {'name': 'noarmor', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'leather', 'cost': 13, 'damage': 0, 'armor': 1},
    {'name': 'chainmail', 'cost': 31, 'damage': 0, 'armor': 2},
    {'name': 'splintmail', 'cost': 53, 'damage': 0, 'armor': 3},
    {'name': 'bandedmail', 'cost': 75, 'damage': 0, 'armor': 4},
    {'name': 'platemail', 'cost': 102, 'damage': 0, 'armor': 5}
]
rings = [
    {'name': 'no ring', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'no ring', 'cost': 0, 'damage': 0, 'armor': 0},
    {'name': 'damage +1', 'cost': 25, 'damage': 1, 'armor': 0},
    {'name': 'damage +2', 'cost': 50, 'damage': 2, 'armor': 0},
    {'name': 'damage +3', 'cost': 100, 'damage': 3, 'armor': 0},
    {'name': 'defense +1', 'cost': 20, 'damage': 0, 'armor': 1},
    {'name': 'defense +2', 'cost': 40, 'damage': 0, 'armor': 2},
    {'name': 'defense +3', 'cost': 80, 'damage': 0, 'armor': 3}
]


# Hit Points: 109
# Damage: 8
# Armor: 2

class Player:
    def __init__(self, hp, damage, armor):
        self.hitpoints = hp
        self.damage = damage
        self.armor = armor


def go():
    # if play(Player(100, 6, 4), Player(109, 8, 2)):
    #     print('win')
    # else:
    #     print('lose')
    min_cost = 9999999
    for weapon in weapons:
        for armor in armors:
            for ring in itertools.permutations(rings, 2):
                cost = weapon['cost'] + armor['cost'] + sum([r['cost'] for r in ring])
                player_1 = Player(100, weapon['damage'] + sum([r['damage'] for r in ring]),
                                  armor['armor'] + sum([r['armor'] for r in ring]))
                opp = Player(109, 8, 2)
                win = play(player_1, opp)
                if win:
                    min_cost = min(cost, min_cost)
    print(min_cost)


def play(player, opp):
    while True:
        opp = Player(opp.hitpoints - max(1, player.damage - opp.armor), opp.damage, opp.armor)
        if opp.hitpoints <= 0:
            return True
        player = Player(player.hitpoints - max(1, opp.damage - player.armor), player.damage, player.armor)
        if player.hitpoints <= 0:
            return False
