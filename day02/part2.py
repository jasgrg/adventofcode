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


class Game:
    def __init__(self):
        self.min_blue = -1
        self.min_red = -1
        self.min_green = -1

    def add_cube(self, cube: Cube):
        if cube.color == 'blue' and cube.count > self.min_blue:
            self.min_blue = cube.count
        if cube.color == 'green' and cube.count > self.min_green:
            self.min_green = cube.count
        if cube.color == 'red' and cube.count > self.min_red:
            self.min_red = cube.count


def go():
    open_file("assets/2_cube_games.txt")
    total = 0
    line_number, l, eof = get_next_line()
    while not eof:
        words = l.split(': ')
        game = words[1].split(' ')
        bag = Game()
        for c in range(0, len(game) - 1, 2):
            cube = Cube(game[c], game[c + 1])
            bag.add_cube(cube)
        total += int(bag.min_blue * bag.min_red * bag.min_green)
        line_number, l, eof = get_next_line()
    print(total)
