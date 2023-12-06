from file_helpers import open_file, get_next_line


class Rule:
    def __init__(self, dest_range_start, source_range_start, length):
        self.source_range_start = source_range_start
        self.source_range_end = source_range_start + length - 1
        self.delta = self.source_range_start - dest_range_start

    def applies(self, value):
        return self.source_range_start <= value <= self.source_range_end

    def get_next(self, value):
        return value - self.delta


class Rules:
    def __init__(self):
        self.rules = []

    def add_rule(self, dest_range_start, source_range_start, length):
        self.rules.append(Rule(dest_range_start, source_range_start, length))

    def calculate_next_val(self, val):
        for r in self.rules:
            if r.applies(val):
                return r.get_next(val)
        return val


def go():
    open_file('assets/5_almanac.txt')
    line_number, l, eof = get_next_line()
    while not eof:
        if l != '':
            if l.startswith("seeds"):
                seeds = [int(s) for s in l.split(' ')[1:len(l.split(' '))]]
            if l.endswith('map:'):
                rules = Rules()
                line_number, l, eof = get_next_line()
                while not eof and l != '':
                    parts = [int(p) for p in l.split(' ')]
                    rules.add_rule(parts[0], parts[1], parts[2])
                    line_number, l, eof = get_next_line()
                for i in range(0, len(seeds)):
                    seeds[i] = rules.calculate_next_val(seeds[i])
        line_number, l, eof = get_next_line()

    min_value = -1
    for s in seeds:
        if min_value == -1 or min_value > s:
            min_value = s
    print(min_value)
