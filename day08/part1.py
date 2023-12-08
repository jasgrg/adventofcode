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

    d = 0
    steps = 0
    cur_node = map.get_node('AAA')
    while True:
        if d == len(directions):
            d = 0
        dir = directions[d]
        if dir == 'R':
            cur_node = map.get_node(cur_node.right)
        if dir == 'L':
            cur_node = map.get_node(cur_node.left)
        steps += 1
        d += 1
        if cur_node.name == 'ZZZ':
            print(str(steps))
            break
