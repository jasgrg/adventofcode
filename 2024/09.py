from file_helpers import read_all_text


def unpack():
    line = [c for c in read_all_text("09.txt")]
    unpacked = []
    file_id = 0
    for idx, n in enumerate(line):
        if idx % 2 == 0:
            for f in range(0, int(n)):
                unpacked.append(file_id)
            file_id += 1
        else:
            for f in range(0, int(n)):
                unpacked.append(-1)
    return unpacked


def part1():
    unpacked = unpack()
    s = 0
    e = len(unpacked) - 1
    while e > s:
        if unpacked[e] != -1:
            while unpacked[s] != -1:
                s += 1
            if s < e:
                unpacked[s], unpacked[e] = unpacked[e], -1
        e -= 1
    total = 0
    print(unpacked)
    for idx, c in enumerate(unpacked):
        if c != -1:
            total += idx * c
    print(total)


def part2():
    line = [c for c in read_all_text("09.txt")]
    unpacked = []
    file_id = 0

    for idx, n in enumerate(line):
        if idx % 2 == 0:
            file = []
            for f in range(0, int(n)):
                file.append(file_id)

            unpacked.append(file)
            file_id += 1
        else:
            space = []
            for f in range(0, int(n)):
                space.append(-1)
            if len(space) > 0:
                unpacked.append(space)
    print(unpacked)
    max_file_id = file_id - 1

    for file in range(max_file_id, 0, -1):
        for check_file in range(len(unpacked) - 1, 0, -1):
            if len(unpacked[check_file]) > 0 and unpacked[check_file][0] == file:
                for space in range(0, check_file):
                    if len(unpacked[space]) > 0 and unpacked[space][0] == -1 and len(unpacked[space]) >= len(
                            unpacked[check_file]):
                        new_file = [f for f in unpacked[check_file]]
                        unpacked.insert(space, new_file)
                        for f in range(0, len(new_file)):
                            unpacked[space + 1].pop()
                        for f in range(0, len(unpacked[check_file + 1])):
                            unpacked[check_file + 1][f] = -1
                        break
                break
    print(unpacked)
    idx = 0
    total = 0
    for f in unpacked:
        for v in f:
            if v != -1:
                total += idx * v
            idx += 1
    print(total)


part2()
