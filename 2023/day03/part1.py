from file_helpers import get_all_lines

numbers = '0123456789'


def is_special_char(char):
    return not char in numbers + '\n.'


def contains_special_char(line, start_index, end_index):
    for c in line[start_index:end_index]:
        if is_special_char(c):
            return True
    return False


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
                if contains_special_char(l, start_index, end_index) or \
                        (line_number > 0 and contains_special_char(lines[line_number - 1], start_index, end_index)) or \
                        (line_number < len(lines) - 1 and contains_special_char(lines[line_number + 1], start_index,
                                                                                end_index)):
                    total += int(num)
            else:
                char_index += 1
        line_number += 1
    print(total)
