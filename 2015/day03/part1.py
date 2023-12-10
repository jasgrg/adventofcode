from file_helpers import open_file, get_next_line


def adjust_coords(cur_position, dir):
    if dir == 'v':
        cur_position['y'] -= 1
    if dir == '^':
        cur_position['y'] += 1
    if dir == '>':
        cur_position['x'] += 1
    if dir == '<':
        cur_position['x'] -= 1


def go():
    open_file("assets/03.txt")
    line_number, l, eof = get_next_line()
    coords = {
        '0:0': 1
    }
    cur_position = {
        'x': 0,
        'y': 0
    }
    for direction in l:
        adjust_coords(cur_position, direction)
        key = str(cur_position['x']) + ':' + str(cur_position['y'])
        if not key in coords:
            coords[key] = 1
        else:
            coords[key] += 1
    print(str(len(coords)))
