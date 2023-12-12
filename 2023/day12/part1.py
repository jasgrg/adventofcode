import itertools

from file_helpers import open_file, get_next_line


def get_replacement_indexes(pattern):
    return [idx for idx, p in enumerate(pattern) if p == '?']


def does_pattern_conform(pattern, counts):
    seqs = []
    seq = 0
    for l in pattern:
        if l == '.':
            if seq > 0:
                seqs.append(seq)
            seq = 0
        else:
            seq += 1
    if seq != 0:
        seqs.append(seq)
    if len(seqs) != len(counts):
        return False
    for s_indx, s in enumerate(seqs):
        if seqs[s_indx] != counts[s_indx]:
            return False
    return True


def find_possible_arrangements(pattern, counts):
    idxs = get_replacement_indexes(pattern)
    total_hashes = sum([c for c in counts])
    permutations = itertools.product('#.', repeat=len(idxs))
    count = 0
    for perm in permutations:
        for perm_index, p in enumerate(perm):
            pattern[idxs[perm_index]] = p
        if len([a for a in pattern if a == '#']) == total_hashes:
            if does_pattern_conform(pattern, counts):
                count += 1

    return count


def go():
    open_file("assets/12.txt")
    line_number, l, eof = get_next_line()
    count = 0
    while not eof:
        sides = l.split(' ')
        pattern = [l for l in sides[0]]
        counts = [int(c) for c in sides[1].split(',')]
        count += find_possible_arrangements(pattern, counts)
        line_number, l, eof = get_next_line()
    print(str(count))
