from file_helpers import get_all_lines
from utlities import Matrix, vector_direction_values, vector_directions, Coord

matrix = Matrix(get_all_lines("12.txt"))
seen = []


def d():
    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if len([s for s in seen if s.equals(Coord(x, y))]) == 0:
                matrix.set(x, y, '.')
    matrix.draw()


def part1():
    def calculate(x, y):
        crop = matrix.get(x, y)
        fnc = 0
        a = 0
        seen.append(Coord(x, y))
        for dir in vector_direction_values:
            check = Coord(dir.x + x, dir.y + y)
            if matrix.is_in_bounds(check.x, check.y):
                if matrix.get(check.x, check.y) != crop:
                    fnc += 1
                elif len([c for c in seen if c.equals(check)]) == 0:
                    ar, fence = calculate(check.x, check.y)
                    fnc += fence
                    a += ar
            else:
                fnc += 1
        return a + 1, fnc

    total = 0
    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if len([s for s in seen if s.equals(Coord(x, y))]) == 0:
                a, f = calculate(x, y)
                total += a * f
    print(total)


# part1()

checks = {
    'n': ['w', 'nw'],
    'e': ['n', 'ne'],
    's': ['w', 'sw'],
    'w': ['n', 'nw']
}


def part2():
    def new_fence(crop, dir, x, y):
        for d in vector_directions:
            if vector_directions[d].equals(dir):
                v1 = vector_directions[checks[d][0]]
                v2 = vector_directions[checks[d][1]]
                c1 = Coord(x, y).add(v1)
                c2 = Coord(x, y).add(v2)
                if not matrix.is_in_bounds(c1.x, c1.y):
                    return 1
                elif matrix.get(c1.x, c1.y) != crop:
                    return 1
                else:
                    if not matrix.is_in_bounds(c2.x, c2.y):
                        return 0
                    else:
                        return 1 if matrix.get(c2.x, c2.y) == crop else 0

    def calculate(x, y):
        crop = matrix.get(x, y)
        fnc = 0
        a = 0
        seen.append(Coord(x, y))
        for dir in vector_direction_values:
            check = Coord(dir.x + x, dir.y + y)
            if matrix.is_in_bounds(check.x, check.y):
                if matrix.get(check.x, check.y) != crop:
                    fnc += new_fence(crop, dir, x, y)
                elif len([c for c in seen if c.equals(check)]) == 0:
                    ar, fence = calculate(check.x, check.y)
                    fnc += fence
                    a += ar
            else:
                fnc += new_fence(crop, dir, x, y)
        return a + 1, fnc

    total = 0
    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if len([s for s in seen if s.equals(Coord(x, y))]) == 0:
                a, f = calculate(x, y)
                total += a * f
    print(total)


part2()
