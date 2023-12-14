from file_helpers import get_all_lines
from utlities import convert_to_matrix


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
    tilt(platform, 'N')
    print(find_weight(platform))
