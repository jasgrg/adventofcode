import re

from file_helpers import open_file, get_next_line


def go():
    open_file("assets/12.txt")
    pattern = re.compile("-?[0-9]+")
    total = 0
    while True:
        line_number, l, eof = get_next_line()
        matches = re.findall(pattern, l)
        for match in matches:
            total += int(match)
        if eof:
            break
    print(total)
