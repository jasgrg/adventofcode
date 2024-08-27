import itertools

from file_helpers import open_file, get_next_line

containers = []
to_store = 150


def go():
    open_file("assets/17.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof:
            break
        containers.append(int(l))
    for i in range(1, len(containers)):
        permutations = [p for p in itertools.combinations(containers, i) if sum(p) == to_store]
        if (len(permutations)) > 0:
            print(len(permutations))
            break
