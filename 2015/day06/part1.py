from file_helpers import open_file, get_next_line
from utlities import Coord


def go():
    open_file("assets/06.txt")

    lights = []

    def turn(start: Coord, end: Coord, on: bool):
        for y in range(start.y, end.y + 1):
            for x in range(start.x, end.x + 1):
                lights[y][x] = on

    def toggle(start: Coord, end: Coord):
        for y in range(start.y, end.y + 1):
            for x in range(start.x, end.x + 1):
                lights[y][x] = not lights[y][x]

    for y in range(0, 1000):
        lights.append([])
        for x in range(0, 1000):
            lights[y].append(False)

    line_number, l, eof = get_next_line()
    while not eof:
        words = l.split(' ')
        if words[0] == 'turn':
            start = words[2].split(',')
            end = words[4].split(',')

            turn(Coord(int(start[0]), int(start[1])), Coord(int(end[0]), int(end[1])), words[1] == 'on')
        else:
            start = words[1].split(',')
            end = words[3].split(',')
            toggle(Coord(int(start[0]), int(start[1])), Coord(int(end[0]), int(end[1])))

        line_number, l, eof = get_next_line()

    count = 0
    for y in lights:
        for x in y:
            if x:
                count += 1
    print(str(count))
