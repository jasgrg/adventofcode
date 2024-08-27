from heapq import heappush, heappop

from utlities import Matrix, Coord, get_distance


class MatrixAStarNode:
    def __init__(self, pos: Coord, value: int, distance_to_goal: int, parent):
        self.value = value
        self.coordinates = pos
        self.previous = parent
        self.distance_to_goal = distance_to_goal
        self.parent = parent
        self.key = f"{self.coordinates.x}_{self.coordinates.y}_{self.value}"
        # if self.parent is not None:
        #     self.key += f"_{self.parent.coordinates.x}_{self.parent.coordinates.y}"

    def __lt__(self, other):
        return self.value < other.value


openq = []
open = {}
closed = {}


def debug(matrix, cur_node):
    debug = matrix.clone()
    n = cur_node
    print(str(cur_node.value))

    while n.parent is not None:
        debug.set(n.coordinates.x, n.coordinates.y, '#')
        n = n.parent
    debug.draw()
    print("")


def search(matrix: Matrix, start: Coord, goal: Coord, get_adjacent_coords):
    start_node = MatrixAStarNode(start, 0, get_distance(start, goal), None)
    heappush(openq, (0, start_node))
    open[start_node.key] = start_node
    while len(openq) > 0:
        val, cur_node = heappop(openq)
        closed[cur_node.key] = cur_node
        del open[cur_node.key]
        debug(matrix, cur_node)
        if goal.x == cur_node.coordinates.x and goal.y == cur_node.coordinates.y:
            return cur_node
        children = get_adjacent_coords(cur_node, matrix)
        for child in children:
            node = MatrixAStarNode(child, (cur_node.value + int(matrix.get(child.x, child.y))),
                                   get_distance(child, goal), cur_node)
            if node.key not in closed:
                if node.key not in open or (
                        open[node.key].value + open[node.key].distance_to_goal) > (
                        node.value + node.distance_to_goal):
                    open[node.key] = node
                    heappush(openq, (node.value, node))
