import re
from functools import reduce

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
CASED_LETTERS = f'{LETTERS}ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CHARACTERS = f'0123456789{CASED_LETTERS}'
VOWELS = 'aeiou'
CONSONANTS = [a for a in LETTERS if a not in VOWELS]


###
# for solving a system of equations of the form:
# a * x + b * x = cx
# a * y + b * y = cy
# https://www.youtube.com/watch?v=jBsC34PxzoM

def cramers(ax, ay, bx, by, cx, cy):
    a = ((cx * by) - (cy * bx)) / ((ax * by) - (ay * bx))
    b = ((ax * cy) - (ay * cx)) / ((ax * by) - (ay * bx))
    return a, b


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def clone(self):
        return Coord(self.x, self.y)

    def to_string(self):
        return f'{self.x}, {self.y}'

    def add(self, other):
        return Coord(self.x + other.x, self.y + other.y)


class Vector:
    def __init__(self, pos: Coord, dir: Coord):
        self.pos = pos
        self.dir = dir

    def move(self):
        self.pos.x += self.dir.x
        self.pos.y += self.dir.y

    def clone(self):
        return Vector(Coord(self.pos.x, self.pos.y), Coord(self.dir.x, self.dir.y))

    def equals(self, other):
        return self.pos.equals(other.pos) and self.dir.equals(other.dir)


class Box:
    def __init__(self, top_left: Coord, bottom_right: Coord):
        self.top_left = top_left
        self.bottom_right = bottom_right

        self.left = self.top_left.x
        self.top = self.top_left.y
        self.right = self.bottom_right.x
        self.bottom = self.bottom_right.y

    def clone(self):
        return Box(Coord(self.top_left.x, self.top_left.y), Coord(self.bottom_right.x, self.bottom_right.y))

    def move(self, dir: Coord):
        return Box(self.top_left.add(dir), self.bottom_right.add(dir))

    def intersects(self, other):
        return not (other.left > self.right
                    or other.right < self.left
                    or other.top > self.bottom
                    or other.bottom < self.top)


vector_directions = {
    'n': Coord(0, -1),
    'e': Coord(1, 0),
    's': Coord(0, 1),
    'w': Coord(-1, 0),
    'ne': Coord(1, -1),
    'nw': Coord(-1, -1),
    'se': Coord(1, 1),
    'sw': Coord(-1, 1)
}

vector_direction_values = [
    Coord(0, -1),
    Coord(1, 0),
    Coord(0, 1),
    Coord(-1, 0)
]


def get_distance(p1: Coord, p2: Coord):
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


# matches at the beginning of the string
def regex_match(s, regex):
    pattern = re.compile(regex)
    return pattern.match(s)


# matches at any point in the string
def regex_search(s, regex):
    pattern = re.compile(regex)
    return pattern.search(s)


def regex_split(split_pattern, s):
    return re.split(split_pattern, s)


# returns all matches
def regex_findall(s, regex):
    pattern = re.compile(regex)
    return pattern.findall(s)


def is_numeric(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def is_a_whole_number(x):
    return float(x).is_integer()


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def draw_matrix(m):
    for r in m:
        print(''.join(str(r)))


class Matrix:
    def __init__(self, lines):
        self.m = []
        for r in lines:
            self.m.append([c for c in r])

    def initialize(self, x_size, y_size, default_value):
        self.m = []
        for x in range(y_size):
            r = []
            for y in range(x_size):
                r.append(default_value)
            self.m.append(r)

    def get(self, x, y):
        return self.m[y][x]

    def set(self, x, y, v):
        self.m[y][x] = v

    def get_rows(self):
        return self.m

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

    def is_in_bounds(self, x, y):
        return 0 <= y < len(self.m) and 0 <= x < len(self.m[y])
