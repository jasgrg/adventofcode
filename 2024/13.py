from file_helpers import get_all_lines


def part1():
    def parse_xy(l):
        l = l.replace("Button A: ", "").replace("Button B: ", "")
        if l[0] != 'X':
            raise Exception
        l = l.replace("X+", "").replace("Y+", "")
        p = l.split(',')
        return int(p[0]), int(p[1])

    def parse_prize(l):
        l = l.replace("Prize: X=", "").replace(" Y=", "")
        p = l.split(',')
        return int(p[0]), int(p[1])

    a_cost = 3
    b_cost = 1
    total_cost = 0
    lines = get_all_lines("13.txt")
    for i in range(0, len(lines), 4):
        ax, ay = parse_xy(lines[i])
        bx, by = parse_xy(lines[i + 1])
        px, py = parse_prize(lines[i + 2])
        min_cost = -1
        for apresses in range(100):
            tx = apresses * ax
            ty = apresses * ay
            if tx > px or ty > py:
                break
            if (px - tx) % bx == 0 and (py - ty) % by == 0 and \
                    (px - tx) / bx == (py - ty) / by:
                bpresses = (px - tx) / bx
                cost = (apresses * a_cost) + (bpresses * b_cost)
                min_cost = min(min_cost, cost) if min_cost != -1 else cost
        if min_cost != -1:
            total_cost += min_cost
    print(total_cost)


def part2():
    def parse_xy(l):
        l = l.replace("Button A: ", "").replace("Button B: ", "")
        if l[0] != 'X':
            raise Exception
        l = l.replace("X+", "").replace("Y+", "")
        p = l.split(',')
        return int(p[0]), int(p[1])

    def parse_prize(l):
        l = l.replace("Prize: X=", "").replace(" Y=", "")
        p = l.split(',')
        return int(p[0]) + 10000000000000, int(p[1]) + 10000000000000

    a_cost = 3
    b_cost = 1
    total_cost = 0
    lines = get_all_lines("13.txt")
    for i in range(0, len(lines), 4):
        ax, ay = parse_xy(lines[i])
        bx, by = parse_xy(lines[i + 1])
        px, py = parse_prize(lines[i + 2])
        a = ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
        b = ((ax * py) - (ay * px)) / ((ax * by) - (ay * bx))
        if a.is_integer() and b.is_integer():
            total_cost += (a * a_cost) + (b * b_cost)
    print(total_cost)


part2()
