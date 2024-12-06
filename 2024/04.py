from file_helpers import get_all_lines
from utlities import Matrix

lines = get_all_lines("04.txt")
matrix = Matrix(lines)
word = "XMAS"
word_size = len(word)
cnt = 0
h_cnt = 0

ddr_cnt = 0
dur_cnt = 0
v_cnt = 0
ddl_cnt = 0
dul_cnt = 0

for y in range(0, matrix.get_row_count()):
    for x in range(0, matrix.get_col_count(y)):
        if matrix.get(x, y) == word[0]:
            off_right_edge = x <= matrix.get_col_count(y) - word_size
            off_left_edge = x >= word_size - 1
            off_bottom = y <= matrix.get_row_count() - word_size
            off_top = y >= word_size - 1
            # check horizontal
            if off_right_edge:
                if f'{matrix.get(x, y)}{matrix.get(x + 1, y)}{matrix.get(x + 2, y)}{matrix.get(x + 3, y)}' == word:
                    h_cnt += 1
                if off_bottom and f'{matrix.get(x, y)}{matrix.get(x + 1, y + 1)}{matrix.get(x + 2, y + 2)}{matrix.get(x + 3, y + 3)}' == word:
                    ddr_cnt += 1
                if off_top and f'{matrix.get(x, y)}{matrix.get(x + 1, y - 1)}{matrix.get(x + 2, y - 2)}{matrix.get(x + 3, y - 3)}' == word:
                    dur_cnt += 1

            if off_left_edge:
                if f'{matrix.get(x, y)}{matrix.get(x - 1, y)}{matrix.get(x - 2, y)}{matrix.get(x - 3, y)}' == word:
                    h_cnt += 1
                if off_bottom and f'{matrix.get(x, y)}{matrix.get(x - 1, y + 1)}{matrix.get(x - 2, y + 2)}{matrix.get(x - 3, y + 3)}' == word:
                    ddl_cnt += 1
                if off_top and f'{matrix.get(x, y)}{matrix.get(x - 1, y - 1)}{matrix.get(x - 2, y - 2)}{matrix.get(x - 3, y - 3)}' == word:
                    dul_cnt += 1
            if off_bottom and f'{matrix.get(x, y)}{matrix.get(x, y + 1)}{matrix.get(x, y + 2)}{matrix.get(x, y + 3)}' == word:
                v_cnt += 1
            if off_top and f'{matrix.get(x, y)}{matrix.get(x, y - 1)}{matrix.get(x, y - 2)}{matrix.get(x, y - 3)}' == word:
                v_cnt += 1
        #     print(matrix.get(c, r))
total = v_cnt + h_cnt + dul_cnt + dur_cnt + ddl_cnt + ddr_cnt
print(total)
cnt = 0
matrix.draw()
for y in range(0, matrix.get_row_count()):
    for x in range(0, matrix.get_col_count(y)):
        off_right_edge = x <= matrix.get_col_count(y) - 3
        off_bottom = y <= matrix.get_row_count() - 3
        if off_right_edge and off_bottom:
            left = f'{matrix.get(x, y)}{matrix.get(x + 1, y + 1)}{matrix.get(x + 2, y + 2)}'
            right = f'{matrix.get(x + 2, y)}{matrix.get(x + 1, y + 1)}{matrix.get(x, y + 2)}'
            if (left == 'MAS' or left == 'SAM') and (right == 'MAS' or right == 'SAM'):
                cnt += 1
print(cnt)
