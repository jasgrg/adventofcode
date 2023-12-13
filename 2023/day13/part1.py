from file_helpers import open_file, get_next_line


def find_mirror(strings, multiplier):
    for indx in range(0, len(strings) - 1):
        if strings[indx] == strings[indx + 1]:
            new_idx = 1
            mirrors = True
            while mirrors and indx + 1 + new_idx < len(strings) and indx - new_idx >= 0:
                if strings[indx + 1 + new_idx] != strings[indx - new_idx]:
                    mirrors = False
                new_idx += 1
            if mirrors:
                return (indx + 1) * multiplier
    return 0


def go():
    open_file("assets/13.txt")
    line_number, l, eof = get_next_line()
    count = 0
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
        x_total = find_mirror(x_strings, 100)
        if x_total == 0:
            total += find_mirror(y_strings, 1)
        else:
            total += x_total

        line_number, l, eof = get_next_line()

    print(str(total))
