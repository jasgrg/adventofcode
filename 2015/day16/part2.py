from file_helpers import open_file, get_next_line


class Aunt:
    def __init__(self, number, values):
        self.number = number
        self.values = values

    def matches(self, stuff):
        for i in stuff.keys():
            if i in self.values:
                if i in ["trees", "cats"]:
                    if self.values[i] < stuff[i]:
                        return False
                elif i in ["pomeranians", "goldfish"]:
                    if self.values[i] > stuff[i]:
                        return False
                elif stuff[i] != self.values[i]:
                    return False
        return True


aunts = []

mfcsam = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def go():
    open_file("assets/16.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof:
            break
        parts = l.split(' ')
        i = 2
        stuff = {}
        while i < len(parts):
            stuff[parts[i].replace(':', '')] = int(parts[i + 1].replace(',', ''))
            i += 2

        aunts.append(Aunt(parts[1].replace(':', ''), stuff))
    for a in aunts:
        if a.matches(mfcsam):
            print(a.number)
