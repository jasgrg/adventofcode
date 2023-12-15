from file_helpers import open_file, get_next_line


def go():
    open_file("assets/15.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        parts = l.split(',')

        for p in parts:
            part_val = 0
            for c in p:
                part_val += ord(c)
                part_val *= 17
                part_val = part_val % 256
            total += part_val
        line_number, l, eof = get_next_line()
    print(total)
