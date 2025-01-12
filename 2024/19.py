from file_helpers import get_all_lines
from utlities import memoize

input = get_all_lines("input.txt")
towels = input[0].split(', ')
towels = sorted(towels, key=len, reverse=True)


def part1():
    @memoize
    def is_valid(pattern):
        if len(pattern) == 0:
            return True
        for towel in towels:
            if len(pattern) >= len(towel) and \
                    pattern.startswith(towel) and \
                    is_valid(pattern[len(towel)::]):
                return True
        return False

    cnt = 0
    for i in range(2, len(input)):
        cnt += 1 if is_valid(input[i]) else 0
    print(cnt)


def part2():
    @memoize
    def is_valid(pattern):

        if len(pattern) == 0:
            return 1
        total = 0
        for towel in towels:
            if len(pattern) >= len(towel) and \
                    pattern.startswith(towel):
                total += is_valid(pattern[len(towel)::])
        return total

    cnt = 0
    for i in range(2, len(input)):
        cnt += is_valid(input[i])
    print(cnt)


part2()
