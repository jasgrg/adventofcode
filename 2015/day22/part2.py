class Player:
    def __init__(self, hp, damage, armor, mana, total_spent):
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.mana = mana
        self.total_spent = total_spent


class Spell:
    def __init__(self, name, duration, cost):
        self.name = name
        self.duration = duration
        self.cost = cost


class Move:
    def __init__(self, player, opponent, effects, next_cast, history):
        self.player = player
        self.opponent = opponent
        self.effects = effects
        self.next_cast = next_cast
        self.history = history


moves = []

spells = [
    Spell('magic_missile', 1, 53),
    Spell('drain', 1, 73),
    Spell('shield', 6, 113),
    Spell('poison', 6, 173),
    Spell('recharge', 5, 229)

]


def go():
    max_cost = 0
    play()


def play():
    # player = Player(10, 0, 0, 250)
    # opponent = Player(14, 8, 0, 0)
    player = Player(50, 0, 0, 500, 0)
    opponent = Player(71, 10, 0, 0, 0)
    min_cost = 9999999999

    for s in spells:
        moves.append(Move(Player(player.hp, player.damage, player.armor, player.mana, player.total_spent),
                          Player(opponent.hp, opponent.damage, opponent.armor, opponent.mana, 0), [],
                          Spell(s.name, s.duration, s.cost), []))

    while len(moves) > 0:
        current_move = moves.pop()
        # print(f"--Player turn-- {current_move.history}")
        # print(
        #     f"player has {current_move.player.hp} hitpoint, {current_move.player.armor} armor, {current_move.player.mana} mana")
        # print(
        #     f"Boss has {current_move.opponent.hp} hitpoint")
        current_move.player.hp -= 1
        if current_move.player.hp <= 0:
            # print("player loses under new rule")
            continue

        apply_spells(current_move)
        if current_move.player.hp <= 0:
            # print("player loses")
            continue
        if current_move.opponent.hp <= 0:
            # print("boss loses")
            min_cost = min(min_cost, current_move.player.total_spent)
            continue

        if current_move.next_cast.cost > current_move.player.mana:
            # print(f"player cannot afford this cast")
            continue
        if len([s for s in current_move.effects if s.name == current_move.next_cast.name]) > 0:
            # print(f"spell already active")
            continue

        # print(f"player casts {current_move.next_cast.name}")
        current_move.player.mana -= current_move.next_cast.cost
        current_move.player.total_spent += current_move.next_cast.cost
        current_move.history.append(current_move.next_cast.name)
        if current_move.next_cast.name == 'magic_missile':
            current_move.opponent.hp -= 4
        elif current_move.next_cast.name == 'drain':
            current_move.opponent.hp -= 2
            current_move.player.hp += 2
        elif current_move.next_cast.name == 'shield':
            current_move.player.armor += 7
            current_move.effects.append(current_move.next_cast)
        else:
            current_move.effects.append(current_move.next_cast)

        if current_move.player.hp <= 0:
            # print("player loses")
            continue
        if current_move.opponent.hp <= 0:
            # print("boss loses")
            min_cost = min(min_cost, current_move.player.total_spent)
            continue

        # print("--Boss turn--")
        # print(
        #     f"player has {current_move.player.hp} hitpoint, {current_move.player.armor} armor, {current_move.player.mana} mana")
        # print(
        #     f"Boss has {current_move.opponent.hp} hitpoint")

        apply_spells(current_move)

        if current_move.player.hp <= 0:
            # print("player loses")
            continue
        if current_move.opponent.hp <= 0:
            # print("boss loses")
            min_cost = min(min_cost, current_move.player.total_spent)
            continue

        # print(f"boss deals {current_move.opponent.damage - current_move.player.armor} damage")
        current_move.player.hp -= max(0, current_move.opponent.damage - current_move.player.armor)

        if current_move.player.hp <= 0:
            # print("player loses")
            continue
        if current_move.opponent.hp <= 0:
            # print("boss loses")
            min_cost = min(min_cost, current_move.player.total_spent)
            continue

        for spell in spells:
            moves.append(Move(
                Player(current_move.player.hp, current_move.player.damage, current_move.player.armor,
                       current_move.player.mana, current_move.player.total_spent),
                Player(current_move.opponent.hp, current_move.opponent.damage, current_move.opponent.armor,
                       current_move.opponent.mana, current_move.opponent.total_spent),
                [Spell(c.name, c.duration, c.cost) for c in current_move.effects],
                Spell(spell.name, spell.duration, spell.cost),
                [c for c in current_move.history]))
    print(min_cost)


def apply_spells(current):
    for spell in current.effects:

        # if spell.name == 'shield':
        # print(f"shield adds 7 to armor its timer is now {spell.duration - 1}")
        if spell.name == 'poison':
            current.opponent.hp -= 3
            # print(f"poison deals 3 damage its timer is now {spell.duration - 1}")
        if spell.name == 'recharge':
            current.player.mana += 101
            # print(f"recharge adds 101 mana its timer is now {spell.duration - 1}")
        spell.duration -= 1
    for c in current.effects:
        if c.duration <= 0:
            if c.name == 'shield':
                current.player.armor -= 7
            # print(f"{c.name} wears off")
    current.effects = [c for c in current.effects if c.duration > 0]
