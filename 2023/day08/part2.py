from math import gcd

from file_helpers import open_file, get_next_line


class MapNode:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def print(self):
        print(self.name + ' => ' + self.left + ' ' + self.right)


class Map:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node(self, name):
        for n in self.nodes:
            if n.name == name:
                return n


def go():
    open_file("assets/8_map.txt")
    line_number, l, eof = get_next_line()
    directions = l
    line_number, l, eof = get_next_line()
    line_number, l, eof = get_next_line()
    map = Map()
    while not eof:
        words = l.split(' ')
        map.add_node(MapNode(words[0], words[2].replace('(', '').replace(',', ''), words[3].replace(')', '')))
        line_number, l, eof = get_next_line()
    path_lengths = []
    direction_index = 0
    step_counter = 0
    ghosts = []
    for n in map.nodes:
        if n.name.endswith('A'):
            ghosts.append(map.get_node(n.name))
    total = len(ghosts)
    while len(path_lengths) < total:
        if direction_index == len(directions):
            direction_index = 0
        direction = directions[direction_index]
        if direction == 'R':
            for g in range(0, len(ghosts)):
                ghosts[g] = map.get_node(ghosts[g].right)
        if direction == 'L':
            for g in range(0, len(ghosts)):
                ghosts[g] = map.get_node(ghosts[g].left)
        step_counter += 1
        direction_index += 1
        for ghost in ghosts:
            if ghost.name.endswith('Z'):
                path_lengths.append(step_counter)
                ghosts = [g for g in ghosts if g.name != ghost.name]

    # find the least common multiple of the lengths of the paths
    lcm = 1
    for i in path_lengths:
        lcm = lcm * i // gcd(lcm, i)
    print(lcm)
