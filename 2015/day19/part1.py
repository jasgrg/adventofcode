from file_helpers import open_file, get_next_line
from utlities import regex_split


class Transition:
    def __init__(self, key, value):
        self.key = key
        self.value = value


transitions = []


def go():
    open_file("assets/19.txt")

    while True:
        line_number, l, eof = get_next_line()
        if eof or l == '':
            break

        parts = l.split(' ')
        transitions.append(Transition(parts[0], parts[2]))
    line_number, molecule, eof = get_next_line()
    results = []
    for test in transitions:
        splits = regex_split(test.key, molecule)
        for i in range(1, len(splits)):
            result = splits[0]
            for j in range(1, len(splits)):
                if i == j:
                    result += test.value + splits[j]
                else:
                    result += test.key + splits[j]
            if result not in results:
                results.append(result)
    print(len(results))
