import itertools

from file_helpers import open_file, get_next_line


class Person:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_potential_neighbor(self, name, happiness):
        self.neighbors[name] = happiness


people = {}


def go():
    open_file("assets/13.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof:
            break
        parts = l.split(' ')
        movement = parts[2]
        amt = int(parts[3])
        if movement == 'lose':
            amt *= -1
        neighbor = parts[10].replace('.', '')
        if parts[0] not in people:
            people[parts[0]] = Person(parts[0])

        person = people[parts[0]]
        person.add_potential_neighbor(neighbor, amt)
    combos = itertools.permutations(people.keys())
    max_score = -1
    for combo in combos:
        total_score = 0
        for idx, p in enumerate(combo):
            if idx == 0:
                total_score += people[p].neighbors[combo[len(combo) - 1]]
            else:
                total_score += people[p].neighbors[combo[idx - 1]]
            if idx == len(combo) - 1:
                total_score += people[p].neighbors[combo[0]]
            else:
                total_score += people[p].neighbors[combo[idx + 1]]
        max_score = max(total_score, max_score)
    print(max_score)
