from file_helpers import open_file, get_next_line


class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def calc(self):
        lw = self.l * self.w
        lh = self.l * self.h
        wh = self.w * self.h

        total = (2 * lw) + (2 * lh) + (2 * wh)
        total += min(lw, min(lh, wh))
        return total


def go():
    open_file("assets/02.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        words = [int(dim) for dim in l.split('x') if dim != '']
        total += Box(words[0], words[1], words[2]).calc()

        line_number, l, eof = get_next_line()
    print(str(total))
