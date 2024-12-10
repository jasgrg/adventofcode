from file_helpers import get_all_lines
from utlities import Matrix, vector_direction_values, Coord

matrix = Matrix(get_all_lines("10.txt"))
score = 0


def part1():
    def calculate_path(x, y, peaks):
        value = int(matrix.get(x, y))
        if value == 9:
            if len([p for p in peaks if p.equals(Coord(x, y))]) == 0:
                peaks.append(Coord(x, y))
        else:
            paths = []
            for dir in vector_direction_values:
                check_dir = Coord(x + dir.x, y + dir.y)
                if matrix.is_in_bounds(check_dir.x, check_dir.y) and int(
                        matrix.get(check_dir.x, check_dir.y)) == value + 1:
                    paths.append(check_dir)
            for p in paths:
                calculate_path(p.x, p.y, peaks)

    score = 0
    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if int(matrix.get(x, y)) == 0:
                peaks = []
                calculate_path(x, y, peaks)
                score += len(peaks)


def part2():
    paths = []
    global score

    def calculate_path(x, y):
        global paths
        global score
        value = int(matrix.get(x, y))
        if value == 9:
            paths.append(Coord(x, y))
            score += 1
        else:
            paths = []
            for dir in vector_direction_values:
                check_dir = Coord(x + dir.x, y + dir.y)
                if matrix.is_in_bounds(check_dir.x, check_dir.y) and int(
                        matrix.get(check_dir.x, check_dir.y)) == value + 1:
                    paths.append(check_dir)
                    calculate_path(check_dir.x, check_dir.y)

    for y in range(0, matrix.get_row_count()):
        for x in range(0, matrix.get_col_count(y)):
            if int(matrix.get(x, y)) == 0:
                paths.append(Coord(x, y))
    for origin in paths:
        calculate_path(origin.x, origin.y)

    print(score)


part2()
