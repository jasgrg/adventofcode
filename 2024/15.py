from file_helpers import get_all_lines
from utlities import Matrix, Coord, vector_directions, Box

lines = get_all_lines("input.txt")

dirs = {
    '<': vector_directions['w'],
    'v': vector_directions['s'],
    '>': vector_directions['e'],
    '^': vector_directions['n']
}


def part1():
    idx = 0
    m = []
    pos = None

    while lines[idx] != '':
        m.append(lines[idx])
        for x in range(0, len(lines[idx])):
            if lines[idx][x] == '@':
                pos = Coord(x, idx)
        idx += 1
    instructions = ''
    while idx < len(lines):
        instructions += lines[idx]
        idx += 1

    def push(pos, v):
        next_pos = pos.add(v)
        if matrix.get(next_pos.x, next_pos.y) == '#':
            return pos
        if matrix.get(next_pos.x, next_pos.y) != '.':
            new = push(next_pos, v)
            if new.equals(next_pos):
                return pos

        matrix.set(next_pos.x, next_pos.y, matrix.get(pos.x, pos.y))
        matrix.set(pos.x, pos.y, '.')
        return next_pos

    matrix = Matrix(m)
    for mv in instructions:
        pos = push(pos, dirs[mv])
        # matrix.draw()

    total = 0
    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if matrix.get(x, y) == 'O':
                total += (100 * y) + x
    print(total)


def part2():
    idx = 0
    m = []
    pos = None
    boxes = []
    walls = []

    while lines[idx] != '':
        m.append(lines[idx].replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.'))
        idx += 1
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x] == '@':
                pos = Box(Coord(x, y), Coord(x, y))
            elif m[y][x] == '[':
                boxes.append(Box(Coord(x, y), Coord(x + 1, y)))
            elif m[y][x] == '#':
                walls.append(Coord(x, y))

    maxx = len(m[0])
    maxy = len(m)
    instructions = ''
    while idx < len(lines):
        instructions += lines[idx]
        idx += 1

    def draw():
        for y in range(0, maxy):
            line = ''
            for x in range(0, maxx):
                matched = False
                if pos.top_left.equals(Coord(x, y)):
                    line += '@'
                    matched = True
                elif len([w for w in walls if w.equals(Coord(x, y)) or w.equals(Coord(x, y))]) > 0:
                    line += '#'
                    matched = True
                else:
                    for idx in range(0, len(boxes)):
                        if boxes[idx].top_left.equals(Coord(x, y)):
                            line += '['
                            matched = True
                        elif boxes[idx].bottom_right.equals(Coord(x, y)):
                            line += ']'
                            matched = True
                if not matched:
                    line += '.'
            print(line)

    def can_move(box, v):
        next = box.move(v)
        if len([w for w in walls if w.equals(next.top_left) or w.equals(next.bottom_right)]) > 0:
            return False

        for idx in range(0, len(boxes)):
            if box is not boxes[idx] and boxes[idx].intersects(next):
                if not can_move(boxes[idx], v):
                    return False
        return True

    def push(box, v):
        if not can_move(box, v):
            return box

        next = box.move(v)
        for idx in range(0, len(boxes)):
            if box is not boxes[idx] and boxes[idx].intersects(next):
                boxes[idx] = push(boxes[idx], v)
        return next

    for mv in instructions:
        pos = push(pos, dirs[mv])
    draw()

    total = 0
    for b in boxes:
        total += (100 * b.top_left.y) + b.top_left.x

    print(total)


part2()
