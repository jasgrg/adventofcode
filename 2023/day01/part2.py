from file_helpers import open_file, get_next_line

numbers = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '0': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'}


def go():
    open_file("assets/1_calibration.txt")
    line_number, l, eof = get_next_line()
    total = 0
    while not eof:
        num = ''
        min_index = -1
        for n in numbers:
            indx = l.find(n)
            if indx > -1:
                if min_index == -1 or indx < min_index:
                    num = numbers[n]
                    min_index = indx
        max_index = -1
        max_num = ''
        for n in numbers:
            indx = l.rfind(n)
            if indx > -1:
                if max_index == -1 or indx > max_index:
                    max_num = numbers[n]
                    max_index = indx
        num += str(max_num)
        total += int(num)
        print(num)
        line_number, l, eof = get_next_line()
    print(total)
