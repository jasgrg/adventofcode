import heapq
import re
from functools import reduce

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
CASED_LETTERS = f'{LETTERS}ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CHARACTERS = f'0123456789{CASED_LETTERS}'
VOWELS = 'aeiou'
CONSONANTS = [a for a in LETTERS if a not in VOWELS]


###
# for solving a system of equations of the form:
# a * x + b * x = cx
# a * y + b * y = cy
# https://www.youtube.com/watch?v=jBsC34PxzoM

def cramers(ax, ay, bx, by, cx, cy):
    a = ((cx * by) - (cy * bx)) / ((ax * by) - (ay * bx))
    b = ((ax * cy) - (ay * cx)) / ((ax * by) - (ay * bx))
    return a, b


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    def clone(self):
        return Coord(self.x, self.y)

    def to_string(self):
        return f'{self.x}, {self.y}'

    def add(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash(self.to_string())

    def __eq__(self, other):
        return self.equals(other)


class Vector:
    def __init__(self, pos: Coord, dir: Coord):
        self.pos = pos
        self.dir = dir

    def move(self):
        self.pos.x += self.dir.x
        self.pos.y += self.dir.y

    def clone(self):
        return Vector(Coord(self.pos.x, self.pos.y), Coord(self.dir.x, self.dir.y))

    def equals(self, other):
        return self.pos.equals(other.pos) and self.dir.equals(other.dir)

    def __eq__(self, other):
        return self.pos == other.pos and self.dir == other.dir

    def __hash__(self):
        return hash(f'{self.pos.to_string()}, {self.dir.to_string()}')

    def __str__(self):
        return self.pos.to_string() + ' ' + vector_direction_arrows[get_direction(self.dir.x, self.dir.y)]


class Box:
    def __init__(self, top_left: Coord, bottom_right: Coord):
        self.top_left = top_left
        self.bottom_right = bottom_right

        self.left = self.top_left.x
        self.top = self.top_left.y
        self.right = self.bottom_right.x
        self.bottom = self.bottom_right.y

    def clone(self):
        return Box(Coord(self.top_left.x, self.top_left.y), Coord(self.bottom_right.x, self.bottom_right.y))

    def move(self, dir: Coord):
        return Box(self.top_left.add(dir), self.bottom_right.add(dir))

    def intersects(self, other):
        return not (other.left > self.right
                    or other.right < self.left
                    or other.top > self.bottom
                    or other.bottom < self.top)


vector_directions = {
    'n': Coord(0, -1),
    'e': Coord(1, 0),
    's': Coord(0, 1),
    'w': Coord(-1, 0),
    'ne': Coord(1, -1),
    'nw': Coord(-1, -1),
    'se': Coord(1, 1),
    'sw': Coord(-1, 1)
}


def get_direction(x, y):
    for v in vector_directions:
        if vector_directions[v] == Coord(x, y):
            return v


vector_direction_values = [
    Coord(0, -1),
    Coord(1, 0),
    Coord(0, 1),
    Coord(-1, 0)
]

vector_direction_arrows = {
    'n': '^',
    'e': '>',
    's': 'v',
    'w': '<'
}


def get_distance(p1: Coord, p2: Coord):
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


# matches at the beginning of the string
def regex_match(s, regex):
    pattern = re.compile(regex)
    return pattern.match(s)


# matches at any point in the string
def regex_search(s, regex):
    pattern = re.compile(regex)
    return pattern.search(s)


def regex_split(split_pattern, s):
    return re.split(split_pattern, s)


# returns all matches
def regex_findall(s, regex):
    pattern = re.compile(regex)
    return pattern.findall(s)


def is_numeric(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def is_a_whole_number(x):
    return float(x).is_integer()


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def draw_matrix(m):
    for r in m:
        print(''.join(str(r)))


class Matrix:
    def __init__(self, lines):
        self.m = []
        for r in lines:
            self.m.append([c for c in r])

    def initialize(self, x_size, y_size, default_value):
        self.m = []
        for x in range(y_size):
            r = []
            for y in range(x_size):
                r.append(default_value)
            self.m.append(r)

    def get(self, x, y):
        return self.m[y][x]

    def set(self, x, y, v):
        self.m[y][x] = v

    def get_rows(self):
        return self.m

    def get_row_count(self):
        return len(self.m)

    def get_col_count(self, row_index):
        return len(self.m[row_index])

    def draw(self):
        for r in self.m:
            print(''.join(r))
        print('')

    def clone(self):
        new_lines = []
        for y in range(0, self.get_row_count()):
            new_line = ''
            for x in range(0, self.get_col_count(y)):
                new_line += self.get(x, y)
            new_lines.append(new_line)
        return Matrix(new_lines)

    def is_in_bounds(self, x, y):
        return 0 <= y < len(self.m) and 0 <= x < len(self.m[y])

    def find(self, v):
        for y in range(0, self.get_row_count()):
            for x in range(0, self.get_col_count(y)):
                if self.get(x, y) == v:
                    return Coord(x, y)
        raise Exception(f"Cannot find {v}")


# class MatrixAStar:
#     def __init__(self, matrix: Matrix, start: Coord, goal: Coord):
#         self.matrix = matrix
#         self.start = start
#         self.goal = goal
#         self.open_list = []
#         self.closed_list = set()


class MatrixAStar:
    class Node:
        def __init__(self, state: Vector, parent=None, cost=0, heuristic=0):
            self.state = state
            self.parent = parent
            self.cost = cost
            self.heuristic = heuristic

        def __lt__(self, other):
            return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __init__(self, matrix: Matrix, start: Vector, goal: Coord):
        self.matrix = matrix
        self.start = start
        self.goal = goal

    def reconstruct_path(self, node: Node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        path.reverse()
        return path

    def cost(self, current_node, neighbor):
        return 1

    def neighbors(self, node: Node):
        return []

    def calculate_heuristic(self, node):
        return get_distance(node.pos, self.goal)

    def debug(self, cur_node):
        debug = self.matrix.clone()
        path = [s.state for s in self.reconstruct_path(cur_node)]

        for p in path:
            debug.set(p.pos.x, p.pos.y, vector_direction_arrows[get_direction(p.dir.x, p.dir.y)])

        debug.draw()

    def search(self):
        open_list = []
        closed_list = set()

        start_node = self.Node(self.start, None, 0, self.calculate_heuristic(self.start))
        heapq.heappush(open_list, start_node)
        while open_list:
            current_node = heapq.heappop(open_list)
            # self.debug(current_node)
            if current_node.state.pos == self.goal:
                return self.reconstruct_path(current_node)
            closed_list.add(current_node.state)

            for neighbor in self.neighbors(current_node):
                if neighbor in closed_list:
                    continue
                neighbor_node = self.Node(state=neighbor,
                                          parent=current_node,
                                          cost=current_node.cost + self.cost(current_node, neighbor),
                                          heuristic=self.calculate_heuristic(neighbor))

                if all(neighbor_node.state != open_node.state for open_node in open_list):
                    heapq.heappush(open_list, neighbor_node)
                else:
                    for open_node in open_list:
                        if neighbor_node.state == open_node.state and neighbor_node.cost < open_node.cost:
                            open_node.parent = current_node
                            open_node.cost = neighbor_node.cost
                            break
        return None


class MatrixAStarWithOverlap:
    class Node:
        def __init__(self, state: Vector, parent=None, cost=0, heuristic=0):
            self.state = state
            self.parent = [parent] if parent is not None else None
            self.cost = cost
            self.heuristic = heuristic

        def __lt__(self, other):
            return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __init__(self, matrix: Matrix, start: Vector, goal: Coord):
        self.matrix = matrix
        self.start = start
        self.goal = goal

    def reconstruct_path(self, node: Node):
        path = []
        while node:
            path.append(node)
            node = node.parent[0] if node.parent is not None else None
        path.reverse()
        return path

    def cost(self, current_node, neighbor):
        return 1

    def neighbors(self, node: Node):
        return []

    def calculate_heuristic(self, node):
        return get_distance(node.pos, self.goal)

    def debug(self, cur_node):
        debug = self.matrix.clone()
        path = [s.state for s in self.reconstruct_path(cur_node)]

        for p in path:
            debug.set(p.pos.x, p.pos.y, vector_direction_arrows[get_direction(p.dir.x, p.dir.y)])

        debug.draw()

    def search_for_all_shortest_paths_with_overlap(self):
        open_list = []
        shortest_paths = []
        min_cost = float('inf')

        start_node = self.Node(self.start, None, 0, self.calculate_heuristic(self.start))
        heapq.heappush(open_list, start_node)
        while open_list:
            current_node = heapq.heappop(open_list)
            if current_node.cost > min_cost:
                continue

            # self.debug(current_node)

            if current_node.state.pos == self.goal:
                path = self.reconstruct_path(current_node)
                if current_node.cost < min_cost:
                    min_cost = current_node.cost
                    shortest_paths = [path]
                elif current_node.cost == min_cost:
                    shortest_paths.append(path)
                print(f'found {len(shortest_paths)} paths')
                continue

            for neighbor in self.neighbors(current_node):
                neighbor_node = self.Node(state=neighbor,
                                          parent=current_node,
                                          cost=current_node.cost + self.cost(current_node, neighbor),
                                          heuristic=self.calculate_heuristic(neighbor))

                if all(neighbor_node.state != open_node.state for open_node in open_list):
                    heapq.heappush(open_list, neighbor_node)
                else:
                    for open_node in open_list:
                        if neighbor_node.state == open_node.state:
                            if neighbor_node.cost < open_node.cost:
                                open_node.parent = [current_node]
                                open_node.cost = neighbor_node.cost
                                break
                            elif neighbor_node.cost == open_node.cost:
                                open_node.parent.append(current_node)
                                break
        return shortest_paths
