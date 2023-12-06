from file_helpers import open_file, get_next_line

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

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
                    num = n
                    min_index = indx
        max_index = -1
        max_num = ''
        for n in numbers:
            indx = l.rfind(n)
            if indx > -1:
                if max_index == -1 or indx > max_index:
                    max_num = n
                    max_index = indx
        num += str(max_num)
        total += int(num)
        print(num)
        line_number, l, eof = get_next_line()
    print(total)