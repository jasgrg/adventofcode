file = None
line_number = 0
lines = []


def read_all_text(file_name):
    with open(file_name) as f:
        return f.read()


def open_file(file_name):
    global lines
    with open(file_name) as f:
        lines = f.readlines()


def get_all_lines(file_name):
    open_file(file_name)
    for i, l in enumerate(lines):
        lines[i] = l.replace('\n', '')
    return lines


def get_next_line():
    global line_number
    if line_number >= len(lines):
        return -1, '', True
    l = lines[line_number].replace('\n', '')
    line_number += 1
    return line_number - 1, l, False
