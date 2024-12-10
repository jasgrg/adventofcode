from itertools import combinations

from file_helpers import get_all_lines
from utlities import Matrix, Coord


def day1():
    matrix = Matrix(get_all_lines("08.txt"))

    frequencies = {}

    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if matrix.get(x, y) != '.':
                if not matrix.get(x, y) in frequencies:
                    frequencies[matrix.get(x, y)] = []
                frequencies[matrix.get(x, y)].append(Coord(int(x), int(y)))

    total = 0
    for freq in frequencies:
        for pair in combinations(frequencies[freq], 2):
            antinode = Coord((pair[0].x - pair[1].x) + pair[0].x, (pair[0].y - pair[1].y) + pair[0].y)
            if 0 <= antinode.x < matrix.get_col_count(0) and \
                    0 <= antinode.y < matrix.get_row_count():
                if matrix.get(antinode.x, antinode.y) != '#':
                    total += 1
                matrix.set(antinode.x, antinode.y, '#')
            antinode = Coord((pair[1].x - pair[0].x) + pair[1].x, (pair[1].y - pair[0].y) + pair[1].y)
            if 0 <= antinode.x < matrix.get_col_count(0) and \
                    0 <= antinode.y < matrix.get_row_count():
                if matrix.get(antinode.x, antinode.y) != '#':
                    total += 1
                matrix.set(antinode.x, antinode.y, '#')
    print(total)


def day2():
    matrix = Matrix(get_all_lines("08.txt"))

    frequencies = {}

    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if matrix.get(x, y) != '.':
                if not matrix.get(x, y) in frequencies:
                    frequencies[matrix.get(x, y)] = []
                frequencies[matrix.get(x, y)].append(Coord(int(x), int(y)))

    total = 0
    for freq in frequencies:
        for pair in combinations(frequencies[freq], 2):
            partner = Coord(pair[1].x, pair[1].y)
            antinode = Coord(pair[0].x, pair[0].y)
            while 0 <= antinode.x < matrix.get_col_count(0) and \
                    0 <= antinode.y < matrix.get_row_count():
                print(total)
                matrix.draw()
                if matrix.get(antinode.x, antinode.y) != '#':
                    total += 1
                matrix.set(antinode.x, antinode.y, '#')

                new_antinode = Coord((antinode.x - partner.x) + antinode.x, (antinode.y - partner.y) + antinode.y)
                partner = Coord(antinode.x, antinode.y)
                antinode = Coord(new_antinode.x, new_antinode.y)

            partner = Coord(pair[0].x, pair[0].y)
            antinode = Coord(pair[1].x, pair[1].y)
            while 0 <= antinode.x < matrix.get_col_count(0) and \
                    0 <= antinode.y < matrix.get_row_count():
                if matrix.get(antinode.x, antinode.y) != '#':
                    total += 1
                matrix.set(antinode.x, antinode.y, '#')

                new_antinode = Coord((antinode.x - partner.x) + antinode.x, (antinode.y - partner.y) + antinode.y)
                partner = Coord(antinode.x, antinode.y)
                antinode = Coord(new_antinode.x, new_antinode.y)

    print(total)
    matrix.draw()


day2()
