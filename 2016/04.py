from file_helpers import get_all_lines
from utlities import LETTERS


def part1():
    total = 0
    for l in get_all_lines("inputs/04.txt"):
        makeup = {

        }
        parts = l.split('[')
        checksum = parts[1].replace(']', '')
        parts = parts[0].split('-')
        section_id = int(parts[-1])
        for p in parts[:-1]:
            for c in p:
                if c in makeup:
                    makeup[c] += 1
                else:
                    makeup[c] = 1
        chars = sorted(makeup.keys(), key=lambda k: (-makeup[k], k), reverse=False)
        match = True
        for c_index in range(len(checksum)):
            if checksum[c_index] != chars[c_index]:
                match = False
        if match:
            total += section_id
    print(total)


def part2():
    def find_letter_index(l):
        for index, c in enumerate(LETTERS):
            if c == l:
                return index
        return -1

    for l in get_all_lines("inputs/04.txt"):
        parts = l.split('[')
        parts = parts[0].split('-')
        section_id = int(parts[-1])
        new_line = ''
        for p in parts[:-1]:
            new_c = ''
            for c in p:
                c_index = (find_letter_index(c) + (section_id % len(LETTERS))) % len(LETTERS)
                new_c += LETTERS[c_index]
            new_line += new_c + ' '
        if new_line.startswith('north'):
            print(f"{new_line} + {section_id}")


part2()
