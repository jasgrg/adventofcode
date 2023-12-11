from file_helpers import open_file, get_next_line
from utlities import Vector, Coord


class Pipe:
    def __init__(self, char):
        self.char = char


def find_next_move(map, v: Vector):
    char = map[v.pos.y][v.pos.x]
    new_dir = v.dir
    if char not in '|-':
        if char == 'F':
            if v.dir.x == -1:
                new_dir = Coord(0, 1)
            else:
                new_dir = Coord(1, 0)
        if char == '7':
            if v.dir.x == 1:
                new_dir = Coord(0, 1)
            else:
                new_dir = Coord(-1, 0)
        if char == 'L':
            if v.dir.y == 1:
                new_dir = Coord(1, 0)
            else:
                new_dir = Coord(0, -1)
        if char == 'J':
            if v.dir.y == 1:
                new_dir = Coord(-1, 0)
            else:
                new_dir = Coord(0, -1)
    return Vector(Coord(v.pos.x + new_dir.x, v.pos.y + new_dir.y), new_dir)


def find_possible_moves(map, pos):
    moves = []
    if pos.x > 0 and map[pos.y][pos.x - 1] in '-FL':
        moves.append(Vector(Coord(pos.x - 1, pos.y), Coord(-1, 0)))
    if pos.y > 0 and map[pos.y - 1][pos.x] in '|F7':
        moves.append(Vector(Coord(pos.x, pos.y - 1), Coord(0, -1)))
    if pos.x < len(map[0]) - 1 and map[pos.y][pos.x + 1] in '-7J':
        moves.append(Vector(Coord(pos.x + 1, pos.y), Coord(1, 0)))
    if pos.y < len(map) - 1 and map[pos.y + 1][pos.x] in '|JL':
        moves.append(Vector(Coord(pos.x, pos.y + 1), Coord(0, 1)))
    return moves


def go():
    open_file("assets/10.txt")
    line_number, l, eof = get_next_line()
    map = []
    pos = Coord(-1, -1)
    while not eof:
        map.append([])
        for idx, p in enumerate(l):
            map[line_number].append(p)
            if p == 'S':
                pos = Coord(idx, line_number)
        line_number, l, eof = get_next_line()

    possible_first_moves = find_possible_moves(map, pos)
    position = possible_first_moves[0]
    dist = 1
    print(str(dist) + ' : ' + map[position.pos.y][position.pos.x])

    while map[position.pos.y][position.pos.x] != 'S':
        position = find_next_move(map, position)
        dist += 1
        print(str(dist) + ' : ' + map[position.pos.y][position.pos.x])
    print(str(dist / 2))
    print(str(possible_first_moves))
