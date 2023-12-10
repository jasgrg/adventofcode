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
    santa_position = {
        'x': 0,
        'y': 0
    }
    robot_position = {
        'x': 0,
        'y': 0
    }
    for idx in range(0, len(l), 2):
        santa_direction = l[idx]
        robot_direction = l[idx + 1]
        adjust_coords(santa_position, santa_direction)
        adjust_coords(robot_position, robot_direction)
        key = str(santa_position['x']) + ':' + str(santa_position['y'])
        if not key in coords:
            coords[key] = 1
        else:
            coords[key] += 1
        key = str(robot_position['x']) + ':' + str(robot_position['y'])
        if not key in coords:
            coords[key] = 1
        else:
            coords[key] += 1
    print(str(len(coords)))
