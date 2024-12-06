import re
from functools import reduce

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
VOWELS = 'aeiou'
CONSONANTS = [a for a in LETTERS if a not in VOWELS]


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


vector_directions = {
    'n': Coord(0, -1),
    'e': Coord(1, 0),
    's': Coord(0, 1),
    'w': Coord(-1, 0)
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
