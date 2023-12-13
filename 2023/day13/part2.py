from file_helpers import open_file, get_next_line


def flip_bit(strings, x, y):
    s = []
    s += strings
    tstr = [l for l in s[x]]
    if tstr[y] == '.':
        tstr[y] = '#'
    else:
        tstr[y] = '.'
    s[x] = ''.join(tstr)
    return s


def find_mirror(strings, ignore_index=-1):
    for indx in range(0, len(strings) - 1):
        if indx != ignore_index:
            if strings[indx] == strings[indx + 1]:
                new_idx = 1
                mirrors = True
                while mirrors and indx + 1 + new_idx < len(strings) and indx - new_idx >= 0:
                    if strings[indx + 1 + new_idx] != strings[indx - new_idx]:
                        mirrors = False
                    new_idx += 1
                if mirrors:
                    return indx
    return -1


def find_mirror_with_flipped_bit(strings, multiplier):
    orig_index = find_mirror(strings)
    for x in range(0, len(strings)):
        for y in range(0, len(strings[x])):
            s = flip_bit(strings, x, y)
            v = find_mirror(s, orig_index)
            if v > -1 and v != orig_index:
                return (v + 1) * multiplier
    return 0


def go():
    open_file("assets/13.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        x_strings = []
        y_strings = []
        for y_indx in range(0, len(l)):
            y_strings.append('')
        while not eof and l != '':
            x_strings.append(l)
            for idx, char in enumerate(l):
                y_strings[idx] += char
            line_number, l, eof = get_next_line()
        x_total = find_mirror_with_flipped_bit(x_strings, 100)
        if x_total == 0:
            y_total = find_mirror_with_flipped_bit(y_strings, 1)
            total += y_total
        else:
            total += x_total

        line_number, l, eof = get_next_line()

    print(str(total))
