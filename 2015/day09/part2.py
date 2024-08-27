from file_helpers import open_file, get_next_line


class Path:
    def __init__(self, city, cost, parent):
        self.city = city
        self.cities = [pc for pc in parent.cities] if parent is not None else []
        if city not in self.cities:
            self.cities.append(city)
        self.total_cost = 0 if parent is None else parent.total_cost + cost
        self.parent = parent


class Route:
    def __init__(self, frm, to, dist):
        self.frm = frm
        self.to = to
        self.dist = int(dist)


class Map:
    def __init__(self):
        self.routes = []
        self.cities = []

    def add_route(self, frm, to, dist):
        self.routes.append(Route(frm, to, dist))
        self.routes.append(Route(to, frm, dist))
        self.add_city(frm)
        self.add_city(to)

    def add_city(self, city):
        for c in self.cities:
            if c == city:
                return
        self.cities.append(city)

    def print(self):
        print("CITIES")
        for c in self.cities:
            print(c)


map = Map()


def go():
    open_file("assets/09.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof:
            break
        tokens = l.split(' ')
        map.add_route(tokens[0], tokens[2], tokens[4])
    map.print()

    paths = [Path(city, 0, None) for city in map.cities]

    p = find_longest_path(paths)
    print(p.total_cost)


def calculate(path):
    paths = []
    if len(path.cities) == len(map.cities):
        return path

    routes = [r for r in map.routes if r.frm == path.city and r.to not in path.cities]
    for r in routes:
        paths.append(Path(r.to, r.dist, path))
    if len(paths) == 0:
        return path
    return find_longest_path(paths)


def find_longest_path(paths):
    max_score = -1
    max_path = None
    for p in paths:
        new_path = calculate(p)
        if max_score == -1 or new_path.total_cost > max_score:
            max_score = new_path.total_cost
            max_path = new_path
    return max_path
