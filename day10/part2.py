from file_helpers import open_file, get_next_line
from utlities import Coord

map = {}
x_size = 0
y_size = 0


class MapPosition:
    def __init__(self, char):
        self.char = char
        self.loop_dir = None
        self.is_loop = False
        self.can_escape = False


def get_map_key(x, y):
    return str(float(x)) + ":" + str(float(y))


def add_to_map(x, y, m: MapPosition):
    map[get_map_key(x, y)] = m


def get_from_Map(x, y):
    key = get_map_key(x, y)
    if key in map:
        return map[key]
    add_to_map(x, y, MapPosition(' '))
    return get_from_Map(x, y)


def find_next_move(v: Coord):
    p = get_from_Map(v.x, v.y)
    char = p.char
    new_dir = p.loop_dir

    if char not in '|-':
        if char == 'F':
            if p.loop_dir.x == -1:
                new_dir = Coord(0, 1)
            else:
                new_dir = Coord(1, 0)
        if char == '7':
            if p.loop_dir.x == 1:
                new_dir = Coord(0, 1)
            else:
                new_dir = Coord(-1, 0)
        if char == 'L':
            if p.loop_dir.y == 1:
                new_dir = Coord(1, 0)
            else:
                new_dir = Coord(0, -1)
        if char == 'J':
            if p.loop_dir.y == 1:
                new_dir = Coord(-1, 0)
            else:
                new_dir = Coord(0, -1)
    np = get_from_Map(v.x + new_dir.x, v.y + new_dir.y)
    np.is_loop = True
    np.loop_dir = new_dir

    squeeze = MapPosition(None)
    squeeze.is_loop = True
    add_to_map(v.x + (.5 * new_dir.x), v.y + (.5 * new_dir.y), squeeze)
    return Coord(v.x + new_dir.x, v.y + new_dir.y)


def find_possible_moves(pos):
    moves = []
    get_from_Map(pos.x, pos.y).loop_dir = Coord(-1, 0)
    get_from_Map(pos.x, pos.y).is_loop = True

    if pos.x > 0 and get_from_Map(pos.x - 1, pos.y).char in '-FL':
        get_from_Map(pos.x - 1, pos.y).loop_dir = Coord(-1, 0)
        get_from_Map(pos.x - 1, pos.y).is_loop = True
        moves.append(Coord(pos.x - 1, pos.y))
    if pos.y > 0 and get_from_Map(pos.x, pos.y - 1).char in '|F7':
        get_from_Map(pos.x, pos.y - 1).loop_dir = Coord(0, -1)
        get_from_Map(pos.x, pos.y - 1).is_loop = True
        moves.append(Coord(pos.x, pos.y - 1))
    if pos.x < x_size - 1 and get_from_Map(pos.x + 1, pos.y).char in '-7J':
        get_from_Map(pos.x + 1, pos.y).loop_dir = Coord(1, 0)
        get_from_Map(pos.x + 1, pos.y).is_loop = True
        moves.append(Coord(pos.x + 1, pos.y))
    if pos.y < y_size - 1 and get_from_Map(pos.x, pos.y + 1).char in '|JL':
        get_from_Map(pos.x, pos.y + 1).loop_dir = Coord(0, 1)
        get_from_Map(pos.x, pos.y + 1).is_loop = True
        moves.append(Coord(pos.x, pos.y + 1))
    for m in moves:
        start_squeeze = MapPosition(' ')
        start_squeeze.is_loop = True
        add_to_map(pos.x + (.5 * (m.x - pos.x)), pos.y + (.5 * (m.y - pos.y)), start_squeeze)
    return moves


def draw_map():
    count = 0
    for y in range(0, y_size):
        outstr = ''
        for x in range(0, x_size):
            p = get_from_Map(x, y)
            if p.is_loop:
                outstr += 'X'
            elif p.can_escape:
                outstr += 'O'
            else:
                count += 1
                outstr += p.char
        print(outstr)
    print(str(count))


def can_escape(x, y):
    if x == 0 or x == x_size - 1:
        return True
    if y == 0 or y == y_size - 1:
        return True
    return get_from_Map(x - 0.5, y).can_escape or \
        get_from_Map(x + 0.5, y).can_escape or \
        get_from_Map(x, y - 0.5).can_escape or \
        get_from_Map(x, y + 0.5).can_escape


def go():
    open_file("assets/10.txt")
    line_number, l, eof = get_next_line()
    global y_size
    global x_size

    while not eof:
        for idx, p in enumerate(l):
            add_to_map(idx, line_number, MapPosition(p))
            if p == 'S':
                pos = Coord(idx, line_number)
        y_size = line_number + 1
        x_size = len(l)
        line_number, l, eof = get_next_line()

    possible_first_moves = find_possible_moves(pos)
    position = possible_first_moves[0]

    while get_from_Map(position.x, position.y).char != 'S':
        position = find_next_move(position)

    added_new = True
    while added_new:
        added_new = False
        y = 0
        while y < y_size:
            x = 0
            while x < x_size:
                p = get_from_Map(x, y)
                if not p.is_loop and not p.can_escape and can_escape(x, y):
                    p.can_escape = True
                    added_new = True
                x += 0.5
            y += 0.5

    draw_map()
