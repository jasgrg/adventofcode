from file_helpers import open_file, get_next_line


def get_cache_key(springs, run_counts, cur_run_size):
    return springs + ":" + str(run_counts) + ":" + str(cur_run_size)


cache = {}


def find_possible_arrangements(springs, run_counts, cur_run_size=0):
    cache_key = get_cache_key(springs, run_counts, cur_run_size)
    if cache_key in cache:
        return cache[cache_key]

    result = None
    if springs == '':
        if len(run_counts) == 1 and cur_run_size == run_counts[0]:
            result = 1
        elif len(run_counts) == 0 and cur_run_size == 0:
            result = 1
        else:
            result = 0
    else:
        first_spring = springs[0]
        springs = springs[1:]
        if len(run_counts) == 1:
            cur_run_size_target = run_counts[0]
            run_counts_leftover = [0]
        else:
            cur_run_size_target, *run_counts_leftover = run_counts
        if first_spring == '?':
            result = find_possible_arrangements('#' + springs, run_counts, cur_run_size) + \
                     find_possible_arrangements('.' + springs, run_counts, cur_run_size)
        elif first_spring == '#':
            if cur_run_size > cur_run_size_target:
                result = 0
            else:
                result = find_possible_arrangements(springs, run_counts, cur_run_size + 1)
        elif first_spring == '.':
            if cur_run_size == 0:
                result = find_possible_arrangements(springs, run_counts, 0)
            elif cur_run_size == cur_run_size_target:
                result = find_possible_arrangements(springs, tuple(run_counts_leftover), 0)
            else:
                result = 0

    cache[cache_key] = result
    return result


def go():
    open_file("assets/12.txt")
    line_number, l, eof = get_next_line()
    count = 0

    while not eof:
        sides = l.split(' ')
        pattern = sides[0]
        for i in range(0, 4):
            pattern += '?' + sides[0]

        run_counts = tuple([int(c) for c in sides[1].split(',')] * 5)
        count += find_possible_arrangements(pattern, run_counts)

        line_number, l, eof = get_next_line()

    print(str(count))
