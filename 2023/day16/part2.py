from file_helpers import get_all_lines
from utlities import Matrix, Vector, Coord

rays = []
energized = []
matrix: Matrix = None


class LightRay:
    def __init__(self, ray_id, v: Vector):
        self.id = ray_id
        self.v = v


def init_energized(matrix):
    global energized
    energized = []
    for row in range(0, matrix.get_row_count()):
        energized.append([])
        for col in range(0, matrix.get_col_count(0)):
            energized[row].append(None)


def set_light_trail(x, y, c: Coord):
    if energized[y][x] is None:
        energized[y][x] = []
    energized[y][x].append(c)


def draw():
    for r in energized:
        outstr = ''
        for c in r:
            if c is not None:
                if len(c) > 1:
                    outstr += str(len(c))
                elif c[0].x == 0:
                    outstr += 'V' if c[0].y == 1 else '^'
                elif c[0].y == 0:
                    outstr += '>' if c[0].x == 1 else '<'
            else:
                outstr += '.'
        print(outstr)
    print('')


def get_dir(dir: Coord):
    if dir.x == 1:
        return 'E'
    if dir.x == -1:
        return 'W'
    if dir.y == 1:
        return 'S'
    if dir.y == -1:
        return 'N'


def set_dir(c: Coord, d):
    if d == 'N':
        c.x = 0
        c.y = -1
    if d == 'S':
        c.x = 0
        c.y = 1
    if d == 'E':
        c.x = 1
        c.y = 0
    if d == 'W':
        c.x = -1
        c.y = 0


def get_next_ray_id():
    global rays
    max_ray_id = -1
    for r in rays:
        if r.id > max_ray_id:
            max_ray_id = r.id
    return max_ray_id + 1


def light_has_been_here_before(v: Vector):
    e = energized[v.pos.y][v.pos.x]
    if e is None or len(e) == 0:
        return False
    for c in e:
        if c.x == v.dir.x and c.y == v.dir.y:
            return True
    return False


def move_ray(ray: LightRay):
    global rays
    ray.v.move()
    if ray.v.pos.x < 0 or ray.v.pos.x >= matrix.get_col_count(0) or \
            ray.v.pos.y < 0 or ray.v.pos.y >= matrix.get_row_count() or \
            light_has_been_here_before(ray.v):
        rays = [r for r in rays if r.id != ray.id]
        return

    dir = get_dir(ray.v.dir)
    m = matrix.get(ray.v.pos.x, ray.v.pos.y)
    set_light_trail(ray.v.pos.x, ray.v.pos.y, Coord(ray.v.dir.x, ray.v.dir.y))
    if m == '.':
        return
    if dir in ['E', 'W']:
        if m == '-':
            return
        if m == '|':
            set_dir(ray.v.dir, 'S')
            new_ray = LightRay(get_next_ray_id(), Vector(Coord(ray.v.pos.x, ray.v.pos.y),
                                                         Coord(ray.v.dir.x, ray.v.dir.y)))
            set_dir(new_ray.v.dir, 'N')
            rays.append(new_ray)
        elif dir == 'E':
            if m == '/':
                set_dir(ray.v.dir, 'N')
            elif m == '\\':
                set_dir(ray.v.dir, 'S')
        elif dir == 'W':
            if m == '/':
                set_dir(ray.v.dir, 'S')
            elif m == '\\':
                set_dir(ray.v.dir, 'N')
    elif dir in ['N', 'S']:
        if m == '|':
            return
        elif m == '-':
            set_dir(ray.v.dir, 'W')
            new_ray = LightRay(get_next_ray_id(), Vector(Coord(ray.v.pos.x, ray.v.pos.y),
                                                         Coord(ray.v.dir.x, ray.v.dir.y)))
            set_dir(new_ray.v.dir, 'E')
            rays.append(new_ray)
        elif dir == 'N':
            if m == '/':
                set_dir(ray.v.dir, 'E')
            elif m == '\\':
                set_dir(ray.v.dir, 'W')
        elif dir == 'S':
            if m == '/':
                set_dir(ray.v.dir, 'W')
            elif m == '\\':
                set_dir(ray.v.dir, 'E')


def run():
    global rays
    while len(rays) > 0:
        ray_index = 0
        while ray_index < len(rays):
            move_ray(rays[ray_index])
            ray_index += 1
        # draw()
        # print('')
        # print('')
    cnt = 0
    for r in energized:
        for c in r:
            if c is not None and len(c) > 0:
                cnt += 1
    return cnt


def go():
    global matrix
    global rays
    matrix = Matrix(get_all_lines("assets/16.txt"))
    # matrix.draw()
    init_energized(matrix)

    max_count = 0
    # print('from the left')
    for init in range(0, matrix.get_col_count(0)):
        rays = []
        init_energized(matrix)
        rays.append(LightRay(0, Vector(Coord(-1, init), Coord(1, 0))))
        cnt = run()
        if cnt > max_count:
            max_count = cnt
        # draw()

    # print('from the right')
    for init in range(0, matrix.get_col_count(0)):
        rays = []
        init_energized(matrix)
        rays.append(LightRay(0, Vector(Coord(matrix.get_col_count(0), init), Coord(-1, 0))))
        cnt = run()
        if cnt > max_count:
            max_count = cnt
        # draw()

    # print('from the top')
    for init in range(0, matrix.get_row_count()):
        rays = []
        init_energized(matrix)
        rays.append(LightRay(0, Vector(Coord(init, -1), Coord(0, 1))))
        cnt = run()
        if cnt > max_count:
            max_count = cnt
        # draw()

    # print('from the bottom')
    for init in range(0, matrix.get_row_count()):
        rays = []
        init_energized(matrix)
        rays.append(LightRay(0, Vector(Coord(init, matrix.get_row_count()), Coord(0, -1))))
        cnt = run()
        if cnt > max_count:
            max_count = cnt

    print(str(max_count))
