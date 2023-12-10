from file_helpers import open_file, get_next_line
from utlities import LETTERS, regex_search

bad = ['ab', 'cd', 'pq', 'xy']


def is_nice(s):
    found = False
    for idx in range(0, len(s) - 1):
        pair = s[idx] + s[idx + 1]
        if s[idx + 2:].find(pair) > -1:
            found = True
            break
    if not found:
        return False

    for l in LETTERS:
        if regex_search(s, f'{l}.{l}'):
            return True
    return False


def go():
    open_file("assets/05.txt")
    line_number, l, eof = get_next_line()
    cnt = 0
    while not eof:
        if is_nice(l):
            cnt += 1

        line_number, l, eof = get_next_line()
    print(str(cnt))
