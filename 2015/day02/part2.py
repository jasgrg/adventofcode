from file_helpers import open_file, get_next_line


class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def calc(self):
        sides = [self.h, self.l, self.w]
        sides.sort()
        total = (2 * sides[0]) + (2 * sides[1])
        return total + (self.l * self.w * self.h)


def go():
    open_file("assets/02.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        words = [int(dim) for dim in l.split('x') if dim != '']
        total += Box(words[0], words[1], words[2]).calc()

        line_number, l, eof = get_next_line()
    print(str(total))
