from file_helpers import get_all_lines
from utlities import Matrix, Coord, MatrixAStar, MatrixAStarWithOverlap, Vector, vector_direction_values

matrix = Matrix(get_all_lines("input.txt"))
start_pos = matrix.find('S')
start = Vector(start_pos, vector_direction_values[1])
end = matrix.find('E')


def part1():
    class ReindeerSearch(MatrixAStar):
        def cost(self, current_node, neighbor_node):
            if current_node is not None:
                if current_node.state.dir == neighbor_node.dir:
                    return 1
                else:
                    return 1001
            else:
                return 1

        def neighbors(self, node: MatrixAStar.Node):
            neighbors = []
            for d in vector_direction_values:
                next = node.state.pos.add(d)
                if (node.parent is None or node.parent.state.pos != next) and matrix.get(next.x,
                                                                                         next.y) != '#':
                    neighbors.append(Vector(next, d))

            return neighbors

        def __init__(self, matrix: Matrix, start: Vector, goal: Coord):
            super().__init__(matrix, start, goal)

    search = ReindeerSearch(matrix, start, end)

    path = search.search()
    print(path[len(path) - 1].cost)


def part2():
    class ReindeerSearch(MatrixAStarWithOverlap):
        def cost(self, current_node, neighbor_node):
            if current_node is not None:
                if current_node.state.dir == neighbor_node.dir:
                    return 1
                else:
                    return 1001
            else:
                return 1

        def neighbors(self, node: MatrixAStarWithOverlap.Node):
            neighbors = []
            for d in vector_direction_values:
                next = node.state.pos.add(d)
                if (node.parent is None or all(p.state.pos != next for p in node.parent)) and matrix.get(next.x,
                                                                                                         next.y) != '#':
                    neighbors.append(Vector(next, d))

            return neighbors

        def __init__(self, matrix: Matrix, start: Vector, goal: Coord):
            super().__init__(matrix, start, goal)

    search = ReindeerSearch(matrix, start, end)

    unique_coords = set()
    paths = search.search_for_all_shortest_paths_with_overlap()
    nodes = []
    parents = []
    for path in paths:
        nodes.append(path[len(path) - 1])
        parents.append(path[len(path) - 1])

    while len(parents) > 0:
        parent = parents.pop(0)
        if parent.parent is not None:
            for p in parent.parent:
                nodes.append(p)
                parents.append(p)

    for n in nodes:
        unique_coords.add(n.state.pos)
    print(len(unique_coords))


part2()
