import re

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
