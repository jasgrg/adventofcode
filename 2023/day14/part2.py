from file_helpers import get_all_lines
from utlities import convert_to_matrix


def to_str(platform):
    s = ''
    for r in platform:
        for c in r:
            s += c
    return s


def tilt(platform, dir):
    if dir == 'N':
        for col_index in range(0, len(platform[0])):
            for row_index in range(0, len(platform)):
                if platform[row_index][col_index] == 'O':
                    check_row = row_index - 1
                    new_row = row_index
                    while check_row >= 0 and platform[check_row][col_index] == '.':
                        new_row = check_row
                        check_row -= 1

                    if new_row != row_index:
                        platform[row_index][col_index] = '.'
                        platform[new_row][col_index] = 'O'

    if dir == 'E':
        for row_index in range(len(platform) - 1, -1, -1):
            for col_index in range(len(platform[0]) - 1, -1, -1):

                if platform[row_index][col_index] == 'O':
                    check_col = col_index + 1
                    new_col = col_index
                    while check_col < len(platform[0]) and platform[row_index][check_col] == '.':
                        new_col = check_col
                        check_col += 1

                    if new_col != col_index:
                        platform[row_index][col_index] = '.'
                        platform[row_index][new_col] = 'O'

    if dir == 'W':
        for row_index in range(0, len(platform)):
            for col_index in range(0, len(platform[0])):

                if platform[row_index][col_index] == 'O':
                    check_col = col_index - 1
                    new_col = col_index
                    while check_col >= 0 and platform[row_index][check_col] == '.':
                        new_col = check_col
                        check_col -= 1

                    if new_col != col_index:
                        platform[row_index][col_index] = '.'
                        platform[row_index][new_col] = 'O'
    if dir == 'S':
        for col_index in range(len(platform[0]) - 1, -1, -1):
            for row_index in range(len(platform) - 1, -1, -1):
                if platform[row_index][col_index] == 'O':
                    check_row = row_index + 1
                    new_row = row_index
                    while check_row < len(platform) and platform[check_row][col_index] == '.':
                        new_row = check_row
                        check_row += 1

                    if new_row != row_index:
                        platform[row_index][col_index] = '.'
                        platform[new_row][col_index] = 'O'


def rotate(platform):
    tilt(platform, 'N')
    tilt(platform, 'W')
    tilt(platform, 'S')
    tilt(platform, 'E')


def find_weight(platform):
    total = 0
    for col_index in range(0, len(platform[0])):
        for row_index in range(0, len(platform)):
            if platform[row_index][col_index] == 'O':
                total += len(platform) - row_index
    return total


def go():
    lines = get_all_lines("assets/14.txt")
    platform = convert_to_matrix(lines)
    history = []
    max_cycle_length = 100
    cycle_length = 0
    idx = 0
    for i in range(0, 1000000000):
        idx = i + 1
        rotate(platform)
        this_iter = to_str(platform)
        if len(history) > max_cycle_length:
            for cycle in range(1, max_cycle_length):
                if this_iter == history[len(history) - cycle]:
                    cycle_length = cycle
                    break
        if cycle_length > 0:
            break
        history.append(this_iter)

    remainder = (1000000000 - idx) % cycle_length

    for leftover in range(0, remainder):
        rotate(platform)

    print(find_weight(platform))
