def go():
    row_number = 1
    max_row = 1
    col_number = 0
    prev = 20151125
    while True:
        new = (prev * 252533) % 33554393
        prev = new
        if row_number == 2946 and col_number == 3028:
            print(new)
            exit(0)
        if row_number == 0:
            row_number = max_row + 1
            max_row = row_number
            col_number = 0
        else:
            col_number += 1
            row_number -= 1
