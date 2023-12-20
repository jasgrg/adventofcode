from file_helpers import open_file, get_next_line


def go():
    open_file("2023/assets/1_calibration.txt")
    line_number, l, eof = get_next_line()
    while not eof:
        line_number, l, eof = get_next_line()
