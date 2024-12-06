from file_helpers import get_all_lines
from utlities import Matrix, Vector, vector_direction_values, Coord

matrix = Matrix(get_all_lines("06.txt"))

guard = None
current_dir = 0
for y in range(0, matrix.get_row_count()):
    for x in range(0, matrix.get_col_count(y)):
        if matrix.get(x, y) == "^":
            guard = Vector(Coord(x, y), vector_direction_values[0])
            current_dur = 0
        elif matrix.get(x, y) == ">":
            guard = Vector(Coord(x, y), vector_direction_values[1])
            current_dur = 1
        elif matrix.get(x, y) == "v":
            guard = Vector(Coord(x, y), vector_direction_values[2])
            current_dur = 2
        elif matrix.get(x, y) == ">":
            guard = Vector(Coord(x, y), vector_direction_values[3])
            current_dur = 3

visited = [guard.pos.clone()]
initial_start = guard.clone()
initial_dir = current_dir


def is_in_bounds(p):
    return 0 <= p.y < matrix.get_row_count() and 0 <= p.x < matrix.get_col_count(p.y)


while True:
    next_move = Coord(guard.pos.x + guard.dir.x, guard.pos.y + guard.dir.y)
    if is_in_bounds(next_move) and matrix.get(next_move.x, next_move.y) == "#":
        current_dir = (current_dir + 1) % 4
        guard.dir = vector_direction_values[current_dir]
    else:
        guard.move()
        if not is_in_bounds(guard.pos):
            break
        else:
            if len([v for v in visited if v.equals(guard.pos)]) == 0:
                visited.append(Coord(guard.pos.x, guard.pos.y))

print(len(visited))
visited = visited[1::]
total = 0
for idx, potential in enumerate(visited):
    current_dir = initial_dir
    print(f'testing {potential.to_string()} {idx}')
    new_guard = initial_start.clone()
    new_visited = [new_guard.clone()]
    new_matrix = matrix.clone()
    new_matrix.set(potential.x, potential.y, '#')
    while True:
        next_move = Coord(new_guard.pos.x + new_guard.dir.x, new_guard.pos.y + new_guard.dir.y)
        if is_in_bounds(next_move) and new_matrix.get(next_move.x, next_move.y) == "#":
            current_dir = (current_dir + 1) % 4
            new_guard.dir = vector_direction_values[current_dir]
        else:
            new_guard.move()
            if not is_in_bounds(new_guard.pos):
                break
            else:
                if len([v for v in new_visited if v.equals(new_guard)]) > 0:
                    total += 1
                    break
                new_visited.append(new_guard.clone())
print(total)
