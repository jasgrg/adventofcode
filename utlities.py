import math
import re
from typing import List

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
VOWELS = 'aeiou'
CONSONANTS = [a for a in LETTERS if a not in VOWELS]


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, pos: Coord, dir: Coord):
        self.pos = pos
        self.dir = dir

    def move(self):
        self.pos.x += self.dir.x
        self.pos.y += self.dir.y


def get_distance(p1: Coord, p2: Coord):
    return math.pow(abs(p2.x - p1.x), 2) + math.pow(abs(p2.y - p1.y), 2)


def regex_match(s, regex):
    pattern = re.compile(regex)
    return pattern.match(s)


def regex_search(s, regex):
    pattern = re.compile(regex)
    return pattern.search(s)


def is_numeric(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def is_a_whole_number(x):
    return float(x).is_integer()


def draw_matrix(m):
    for r in m:
        print(''.join(str(r)))


class Matrix:
    def __init__(self, lines):
        self.m = []
        for r in lines:
            self.m.append([c for c in r])

    def get(self, x, y):
        return self.m[y][x]

    def set(self, x, y, v):
        self.m[y][x] = v

    def get_row_count(self):
        return len(self.m)

    def get_col_count(self, row_index):
        return len(self.m[row_index])

    def draw(self):
        for r in self.m:
            print(''.join(r))
        print('')

    def clone(self):
        new_lines = []
        for y in range(0, self.get_row_count()):
            new_line = ''
            for x in range(0, self.get_col_count(y)):
                new_line += self.get(x, y)
            new_lines.append(new_line)
        return Matrix(new_lines)


class MatrixAStarNode:
    def __init__(self, pos: Coord, value: int, distance_to_goal: int, parent):
        self.value = value
        self.coordinates = pos
        self.previous = parent
        self.distance_to_goal = distance_to_goal
        self.parent = parent


def get_from_list(list: List[MatrixAStarNode], node: Coord):
    for l in list:
        if l.coordinates.x == node.x and \
                l.coordinates.y == node.y:
            return l
    return None


class MatrixAStar:
    def __init__(self, matrix: Matrix, start: Coord, goal: Coord):
        self.matrix = matrix
        self.open = []
        self.closed = []
        self.open.append(MatrixAStarNode(start, 0, get_distance(start, goal), None))
        self.start = start
        self.goal = goal
        self.debug_matrix: Matrix = self.matrix.clone()

    def debug(self, cur_node):

        debug = self.matrix.clone()
        n = cur_node
        print(str(cur_node.value))

        while n.parent is not None:
            debug.set(n.coordinates.x, n.coordinates.y, '#')
            n = n.parent
        debug.draw()
        print("")
        self.debug_matrix.set(cur_node.coordinates.x, cur_node.coordinates.y, '.')
        self.debug_matrix.draw()

    def get_cur_node(self):
        min_value = None
        min_node = None
        for o in self.open:
            if min_value is None or o.value < min_value:
                min_value = o.value
                min_node = o
        return min_node

    def go(self, get_adjacent_coords):
        while len(self.open) > 0:
            cur_node = self.get_cur_node()

            self.open.remove(cur_node)
            self.closed.append(cur_node)

            print(str(len(self.open)))
            print(str(len(self.closed)))
            print('')

            if self.goal.x == cur_node.coordinates.x and self.goal.y == cur_node.coordinates.y:
                return cur_node
            children = get_adjacent_coords(cur_node, self.matrix)
            for child in children:
                if not get_from_list(self.closed, child):
                    node = MatrixAStarNode(child, (cur_node.value + int(self.matrix.get(child.x, child.y))),
                                           get_distance(child, self.goal), cur_node)
                    in_open = get_from_list(self.open, child)
                    if in_open is None or (in_open.value + in_open.distance_to_goal) <= (
                            node.value + node.distance_to_goal):
                        self.open.append(node)
