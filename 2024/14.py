import statistics

from file_helpers import get_all_lines
from utlities import Vector, Coord, Matrix

lines = get_all_lines("14.txt")
seconds = 100
boardx = 101
boardy = 103

midx = boardx // 2
midy = boardy // 2


def create_and_draw_matrix(bots):
    matrix = Matrix([])
    matrix.initialize(boardx, boardy, '.')
    for b in bots:
        cnt = 0
        if matrix.get(b.pos.x, b.pos.y) != '.':
            cnt = int(matrix.get(b.pos.x, b.pos.y))
        matrix.set(b.pos.x, b.pos.y, str(cnt + 1))
    matrix.draw()


def part1():
    quadrant = [0, 0, 0, 0]
    for l in lines:
        parts = l.split(' v=')
        start_parts = parts[0].replace('p=', '').split(',')
        startx, starty = int(start_parts[0]), int(start_parts[1])

        velo_parts = parts[1].split(',')
        velox, veloy = int(velo_parts[0]), int(velo_parts[1])

        finalx = (startx + (seconds * velox)) % boardx
        finaly = (starty + (seconds * veloy)) % boardy

        if finalx < midx and finaly < midy:
            quadrant[0] += 1
        elif finalx > midx and finaly < midy:
            quadrant[1] += 1
        elif finalx < midx and finaly > midy:
            quadrant[2] += 1
        elif finalx > midx and finaly > midy:
            quadrant[3] += 1

    print(quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3])


def part2():
    bots = []
    for l in lines:
        parts = l.split(' v=')
        start_parts = parts[0].replace('p=', '').split(',')
        startx, starty = int(start_parts[0]), int(start_parts[1])

        velo_parts = parts[1].split(',')
        velox, veloy = int(velo_parts[0]), int(velo_parts[1])
        bots.append(Vector(Coord(startx, starty), Coord(velox, veloy)))

    seconds = 0
    while True:
        seconds += 1
        for b in bots:
            b.move()
            b.pos.x = b.pos.x % boardx
            b.pos.y = b.pos.y % boardy
        xvar = statistics.variance([bot.pos.x for bot in bots])
        yvar = statistics.variance([bot.pos.y for bot in bots])
        clustered = xvar < 400 and yvar < 400

        if clustered:
            print(seconds)
            create_and_draw_matrix(bots)
        elif seconds % 1000 == 0:
            print(f'{seconds} seconds')


part2()
# matrix.draw()
