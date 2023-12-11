from file_helpers import open_file, get_next_line


def go():
    open_file("assets/4_scratchcards.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        parts = l.split(':')
        sides = parts[1].split('|')

        winning_numbers = [int(s) for s in sides[0].split(' ') if s != '']
        my_numbers = [int(s) for s in sides[1].split(' ') if s != '']
        matches = [m for m in my_numbers if m in winning_numbers]
        score = 0 if len(matches) == 0 else pow(2, len(matches) - 1)
        total += score
        line_number, l, eof = get_next_line()
    print(total)
