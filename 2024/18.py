from file_helpers import get_all_lines
from utlities import Matrix, Coord, MatrixAStar, Vector


class Program(MatrixAStar):

    def __init__(self, matrix: Matrix, start: Vector, goal: Coord):
        super().__init__(matrix, start, goal)


lines = get_all_lines("input.txt")

coords = []
for l in lines:
    parts = l.split(',')
    coords.append(Coord(int(parts[0]), int(parts[1])))


def part1():
    matrix = Matrix([])

    x_size = 70
    y_size = 70
    max_bytes = 2952

    matrix.initialize(x_size + 1, y_size + 1, '.')

    for b in range(0, max_bytes):
        matrix.set(coords[b].x, coords[b].y, '#')

    prgrm = Program(matrix, Vector(Coord(0, 0), Coord(0, 1)), Coord(x_size, y_size))
    path = prgrm.search()
    prgrm.debug(path[len(path) - 1])

    print(path[len(path) - 1].cost)


def part2():
    start = 1024
    end = len(coords)
    while True:

        idx = ((end - start) // 2) + start
        print(f"{start} : {end} -> {idx}")
        matrix = Matrix([])

        x_size = 70
        y_size = 70

        matrix.initialize(x_size + 1, y_size + 1, '.')

        for b in range(0, idx):
            matrix.set(coords[b].x, coords[b].y, '#')

        prgrm = Program(matrix, Vector(Coord(0, 0), Coord(0, 1)), Coord(x_size, y_size))
        path = prgrm.search()

        if path is None:
            if end - start < 1:
                print(f'terminated at {idx} : {coords[idx - 1].x}, {coords[idx - 1].y}')

                break
            end = idx
        else:
            start = idx + 1


part2()
