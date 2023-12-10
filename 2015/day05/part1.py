from file_helpers import open_file, get_next_line
from utlities import VOWELS, LETTERS

bad = ['ab', 'cd', 'pq', 'xy']


def is_nice(s):
    vowel_count = len([a for a in s if a in VOWELS])
    if vowel_count < 3:
        return False

    for b in bad:
        if b in s:
            return False
    for l in LETTERS:
        pair = l + l
        if pair in s:
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
