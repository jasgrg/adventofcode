import itertools

from file_helpers import open_file, get_next_line


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


ingredients = []


def go():
    open_file("assets/15.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof:
            break
        parts = l.split(' ')
        ingredients.append(Ingredient(parts[0].replace(':', ''),
                                      int(parts[2].replace(',', '')),
                                      int(parts[4].replace(',', '')),
                                      int(parts[6].replace(',', '')),
                                      int(parts[8].replace(',', '')),
                                      int(parts[10].replace(',', ''))))
    max_score = 0
    numbers = [x for x in range(1, 100)]
    combos = [c for c in itertools.combinations_with_replacement(numbers, len(ingredients)) if sum(c) == 100]
    ingredient_permutations = [p for p in itertools.permutations(ingredients) if
                               len(p) == len(ingredients)]

    for combo in combos:
        for perm in ingredient_permutations:
            capacity_score = 0
            durability_score = 0
            flavor_score = 0
            texture_score = 0
            calories = 0
            for idx, ingredient in enumerate(perm):
                capacity_score += ingredient.capacity * combo[idx]
                durability_score += ingredient.durability * combo[idx]
                flavor_score += ingredient.flavor * combo[idx]
                texture_score += ingredient.texture * combo[idx]
                calories += ingredient.calories * combo[idx]
            score = max(0, capacity_score) * max(0, flavor_score) * max(0, texture_score) * max(0, durability_score)
            if calories == 500:
                max_score = max(max_score, score)
    print(max_score)
