from file_helpers import get_all_lines

numbers = '0123456789'

gear_map = {}
gears = []


def add_part(line_number, index, value):
    key = str(line_number) + "_" + str(index)
    if key in gear_map:
        gears.append(key)
        gear_map[key] *= value
    else:
        gear_map[key] = value


def is_special_char(char):
    return not char in numbers + '\n.'


def contains_special_char(line, start_index, end_index):
    for c in range(start_index, end_index):
        if is_special_char(line[c]):
            return c
    return -1


def go():
    lines = get_all_lines("assets/3_schematic.txt")
    line_number = 0
    total = 0
    while line_number < len(lines):
        l = lines[line_number]
        char_index = 0
        while char_index < len(l) - 1:
            num = ''
            if l[char_index] in numbers:
                start_index = max(0, char_index - 1)
                while l[char_index] in numbers:
                    num += l[char_index]
                    char_index += 1
                end_index = min(char_index + 1, len(l))
                part_index = contains_special_char(l, start_index, end_index)
                if part_index > -1:
                    add_part(line_number, part_index, int(num))
                if line_number > 0 and part_index == -1:
                    part_index = contains_special_char(lines[line_number - 1], start_index, end_index)
                    if part_index > -1:
                        add_part(line_number - 1, part_index, int(num))
                if line_number < len(lines) - 1 and part_index == -1:
                    part_index = contains_special_char(lines[line_number + 1], start_index, end_index)
                    if part_index > -1:
                        add_part(line_number + 1, part_index, int(num))
            else:
                char_index += 1
        line_number += 1
    for g in gears:
        total += gear_map[g]
    print(total)
