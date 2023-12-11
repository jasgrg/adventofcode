from file_helpers import open_file, get_next_line


class Cube:
    def __init__(self, count, color):
        self.count = int(count)
        self.color = color.replace(',', '').replace(';', '')

    def is_valid(self):
        if self.color == 'blue':
            return self.count <= 14
        if self.color == 'red':
            return self.count <= 12
        if self.color == 'green':
            return self.count <= 13


def go():
    open_file("assets/2_cube_games.txt")
    total = 0
    line_number, l, eof = get_next_line()
    while not eof:
        words = l.split(': ')
        game_id = words[0].split(' ')[1]
        game = words[1].split(' ')
        is_valid = True
        for c in range(0, len(game) - 1, 2):
            cube = Cube(game[c], game[c + 1])
            if not cube.is_valid():
                is_valid = False
        if is_valid:
            total += int(game_id)
        line_number, l, eof = get_next_line()
    print(total)
