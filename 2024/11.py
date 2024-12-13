from file_helpers import get_all_lines

line = get_all_lines("11.txt")[0]

rocks = line.split(' ')
blinks = 75


def memoize(f):
    cache = {}

    def foo(x, y):
        key = f"{x}:{y}"
        if key not in cache:
            cache[key] = f(x, y)
        return cache[key]

    return foo


def expand_all(rocks, blink):
    total = 0
    for r in rocks:
        total += expand(r, blink)
    return total


@memoize
def expand(r, blink):
    global total
    if blink == blinks:
        return 1
    if r == '0':
        return expand("1", blink + 1)
    elif len(r) % 2 == 0:
        return expand(str(int(r[:len(r) // 2])), blink + 1) + \
            expand(str(int(r[len(r) // 2:])), blink + 1)
    else:
        return expand(str(int(r) * 2024), blink + 1)


total = expand_all(rocks, 0)
print(total)