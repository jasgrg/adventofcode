from file_helpers import open_file, get_next_line

'''
""
"abc"
"aaa\"aaa"
"\x27"
'''


def go():
    open_file("assets/08.txt")
    total = 0
    line_number, l, eof = get_next_line()
    while not eof:
        actual = len(l)
        encoded = len(l.replace('\\', '\\\\').replace('"', '\\"')) + 2
        total += encoded - actual
        line_number, l, eof = get_next_line()
    print(str(total))
