import itertools

from file_helpers import open_file, get_next_line


def go():
    open_file("assets/24.txt")
    pkgs = []
    while True:
        line_number, l, eof = get_next_line()
        if eof:
            break
        pkgs.append(int(l))

    target = sum(pkgs) // 4
    for i in range(len(pkgs)):
        possible = [c for c in itertools.combinations(pkgs, i) if sum(c) == target]
        if (len(possible)) > 0:
            min_qe = -1
            for p in possible:
                qe = 1
                for q in p:
                    qe *= q
                min_qe = min(min_qe, qe) if min_qe != -1 else qe
            print(min_qe)

            break
