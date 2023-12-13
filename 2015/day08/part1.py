import re

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
        memory = len(
            re.sub('~~[a-z0-9]{2}', 'l',
                   l[1:len(l) - 1].replace('\\\\', '&').replace('\\\"', '%').replace('\\x', '~~')))

        total += actual - memory
        line_number, l, eof = get_next_line()
    print(str(total))
