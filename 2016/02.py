from file_helpers import get_all_lines
from utlities import Matrix

lines = get_all_lines("inputs/02.txt")


def part1():
    code = ''
    m = Matrix([
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ])
    x = y = 1
    for l in lines:
        for d in l:
            if d == 'L':
                x = max(0, x - 1)
            if d == 'R':
                x = min(2, x + 1)
            if d == 'U':
                y = max(0, y - 1)
            if d == 'D':
                y = min(2, y + 1)
        code += m.get(x, y)
    print(code)


def part2():
    code = ''
    m = Matrix([
        ['', '', '1', '', ''],
        ['', '2', '3', '4', ''],
        ['5', '6', '7', '8', '9'],
        ['', 'A', 'B', 'C', ''],
        ['', '', 'D', '', '']
    ])
    x = 0
    y = 2
    for l in lines:
        for d in l:
            new_x = x
            new_y = y
            if d == 'L':
                new_x = max(0, x - 1)
            if d == 'R':
                new_x = min(4, x + 1)
            if d == 'U':
                new_y = max(0, y - 1)
            if d == 'D':
                new_y = min(4, y + 1)
            if m.get(new_x, new_y) != '':
                x = new_x
                y = new_y
        code += m.get(x, y)
    print(code)


part2()
