from file_helpers import get_all_lines
from utlities import Matrix


def calculate_next_matrix(matrix: Matrix):
    new = matrix.clone()

    for x in range(new.get_row_count()):
        for y in range(new.get_col_count(x)):
            lights_on = 0

            for check_x in range(max(0, x - 1), min(new.get_row_count(), x + 2)):
                for check_y in range(max(0, y - 1), min(new.get_col_count(x), y + 2)):
                    if check_x == x and check_y == y:
                        continue
                    lights_on += 1 if matrix.get(check_x, check_y) == '#' else 0
            if new.get(x, y) == '#' and lights_on not in [2, 3]:
                new.set(x, y, '.')
            elif new.get(x, y) == '.' and lights_on == 3:
                new.set(x, y, '#')
    return new


def go():
    matrix = Matrix(get_all_lines("assets/18.txt"))

    steps = 100
    for i in range(steps):
        matrix = calculate_next_matrix(matrix)
    total = 0
    for x in range(matrix.get_row_count()):
        for y in range(matrix.get_col_count(x)):
            total += 1 if matrix.get(x, y) == '#' else 0
    print(total)
