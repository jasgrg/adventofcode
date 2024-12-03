from file_helpers import get_all_lines


def part1():
    map = []

    lines = get_all_lines("inputs/06.txt")

    for i in range(8):
        map.append({})

    for l in lines:
        for indx, c in enumerate(l):
            if c not in map[indx]:
                map[indx][c] = 1
            else:
                map[indx][c] += 1

    signal = ''
    for m in map:
        signal += sorted(m.keys(), key=lambda k: m[k], reverse=True)[0]
    print(signal)


def part2():
    map = []

    lines = get_all_lines("inputs/06.txt")

    for i in range(8):
        map.append({})

    for l in lines:
        for indx, c in enumerate(l):
            if c not in map[indx]:
                map[indx][c] = 1
            else:
                map[indx][c] += 1

    signal = ''
    for m in map:
        signal += sorted(m.keys(), key=lambda k: m[k])[0]
    print(signal)


part2()
