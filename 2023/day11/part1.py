from file_helpers import open_file, get_next_line
from utlities import Coord

# part 1 and 2 use this same code
# for part 1 this value is 2, for part 2 this value is 1000000
expansion = 1000000


class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.orig = Coord(x, y)


stars = []

map = []


def go():
    open_file("assets/11.txt")
    line_number, l, eof = get_next_line()
    y = 0
    while not eof:
        map.append([])
        found_star = False
        for x_index, c in enumerate(l):
            map[line_number].append(c)
            if c != '.':
                found_star = True
                stars.append(Star(x_index, y))

        y += 1
        if not found_star:
            y += expansion - 1
        line_number, l, eof = get_next_line()

    for x_index, row in enumerate(map[0]):
        found_star = False
        for y_index, c in enumerate(map):
            if map[y_index][x_index] != '.':
                found_star = True

        if not found_star:
            for s in stars:
                if s.orig.x > x_index:
                    s.x += expansion - 1

    dist = 0
    for s in range(0, len(stars) - 1):
        for s1 in range(s + 1, len(stars)):
            d = abs(stars[s1].x - stars[s].x) + abs(stars[s1].y - stars[s].y)
            dist += d
    print(str(dist))
