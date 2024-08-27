from file_helpers import read_all_text
from utlities import vector_directions, Vector, Coord, get_distance

dirs = [vector_directions['n'], vector_directions['e'], vector_directions['s'], vector_directions['w']]
input = read_all_text("inputs/01.txt")

parts = input.split(' ')
parts = [c.replace(',', '') for c in parts]

# part 1
dir_index = 0
current = Vector(Coord(0, 0), vector_directions['n'])
for m in parts:
    if m[0] == 'R':
        dir_index = (dir_index + 1) % len(dirs)
    elif m[0] == 'L':
        dir_index = dir_index - 1
        if dir_index < 0:
            dir_index = len(dirs) - 1
    current.dir = dirs[dir_index]
    for i in range(int(m[1:])):
        current.move()
print(get_distance(Coord(0, 0), current.pos))

# part 2
dir_index = 0
current = Vector(Coord(0, 0), vector_directions['n'])
visited = []
for m in parts:
    if m[0] == 'R':
        dir_index = (dir_index + 1) % len(dirs)
    elif m[0] == 'L':
        dir_index = dir_index - 1
        if dir_index < 0:
            dir_index = len(dirs) - 1
    current.dir = dirs[dir_index]
    for i in range(int(m[1:])):
        current.move()

        if len([c for c in visited if c.x == current.pos.x and c.y == current.pos.y]) > 0:
            print(get_distance(Coord(0, 0), current.pos))
            exit(0)
        visited.append(Coord(current.pos.x, current.pos.y))
