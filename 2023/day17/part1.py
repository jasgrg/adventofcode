from typing import List

from algs.astar import search, MatrixAStarNode
from file_helpers import get_all_lines
from utlities import Matrix, Coord


def get_direction(p1: Coord, p2: Coord):
    if p1.x == p2.x:
        return 'N' if p1.y < p2.y else 'S'
    else:
        return 'W' if p1.x < p2.x else 'E'


def get_possible_moves(node: MatrixAStarNode, matrix: Matrix) -> List[Coord]:
    # if node.coordinates.x == 2 and node.coordinates.y == 0:
    #     breakpoint()
    blocked_dir = ''
    prev_dir = ''
    if node.parent is not None and node.parent.parent is not None and node.parent.parent.parent is not None:
        prev_dir = get_direction(node.coordinates, node.parent.coordinates)
        if prev_dir == get_direction(node.parent.coordinates, node.parent.parent.coordinates) and \
                prev_dir == get_direction(node.parent.parent.coordinates, node.parent.parent.parent.coordinates):
            blocked_dir = prev_dir
    prev_dir = ''
    possible = []
    if node.coordinates.y > 0 and blocked_dir != 'N' and prev_dir != 'S':
        possible.append(Coord(node.coordinates.x, node.coordinates.y - 1))
    if node.coordinates.y < matrix.get_row_count() - 1 and blocked_dir != 'S' and prev_dir != 'N':
        possible.append(Coord(node.coordinates.x, node.coordinates.y + 1))
    if node.coordinates.x > 0 and blocked_dir != 'W' and prev_dir != 'E':
        possible.append(Coord(node.coordinates.x - 1, node.coordinates.y))
    if node.coordinates.x < matrix.get_col_count(0) - 1 and blocked_dir != 'E' and prev_dir != 'W':
        possible.append(Coord(node.coordinates.x + 1, node.coordinates.y))

    return possible


def go():
    matrix = Matrix(get_all_lines("assets/17.txt"))
    result = search(matrix, Coord(0, 0), Coord(matrix.get_col_count(0) - 1, matrix.get_row_count() - 1),
                    get_possible_moves)
    print(result.value)
    while node.parent is not None:
        matrix.set(node.coordinates.x, node.coordinates.y, '#')
        node = node.parent
    matrix.draw()
    print(node.value)
