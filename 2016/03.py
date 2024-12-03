from file_helpers import get_all_lines


def part1():
    lines = get_all_lines("inputs/03.txt")
    cnt = 0
    for l in lines:
        s = [int(c) for c in l.split(' ') if c != '']
        cnt += 1 if s[0] + s[1] > s[2] and s[1] + s[2] > s[0] and s[2] + s[0] > s[1] else 0

    print(cnt)


def part2():
    lines = get_all_lines("inputs/03.txt")
    cnt = 0
    i = 0
    while i < len(lines):
        a = [int(n) for n in lines[i].split(' ') if n != '']
        i += 1
        b = [int(n) for n in lines[i].split(' ') if n != '']
        i += 1
        c = [int(n) for n in lines[i].split(' ') if n != '']
        i += 1

        cnt += 1 if a[0] + b[0] > c[0] and b[0] + c[0] > a[0] and c[0] + a[0] > b[0] else 0
        cnt += 1 if a[1] + b[1] > c[1] and b[1] + c[1] > a[1] and c[1] + a[1] > b[1] else 0
        cnt += 1 if a[2] + b[2] > c[2] and b[2] + c[2] > a[2] and c[2] + a[2] > b[2] else 0

    print(cnt)


part2()
