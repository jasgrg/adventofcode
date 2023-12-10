from file_helpers import open_file, get_next_line


def go():
    open_file("assets/01.txt")
    line_number, l, eof = get_next_line()
    floor = 0
    for dir in l:
        if dir == '(':
            floor += 1
        elif dir == ')':
            floor -= 1
    print(str(floor))
