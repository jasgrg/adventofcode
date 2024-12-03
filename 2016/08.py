import file_helpers
from utlities import Matrix

scn = Matrix([])
scn.initialize(50, 6, '.')
for l in file_helpers.get_all_lines("inputs/08.txt"):
    p = l.split(' ')
    if p[0] == 'rect':
        dims = p[1].split('x')
        for x in range(int(dims[0])):
            for y in range(int(dims[1])):
                scn.set(x, y, '#')
    if p[0] == 'rotate':
        if p[1] == "column":
            col = int(p[2].split('=')[1])
            val = int(p[4])
            original_values = []
            for indx in range(scn.get_row_count()):
                original_values.append(scn.get(col, indx))
            for indx in range(scn.get_row_count()):
                scn.set(col, (indx + val) % scn.get_row_count(), original_values[indx])
        if p[1] == "row":
            row = int(p[2].split('=')[1])
            val = int(p[4])
            original_values = []
            for indx in range(scn.get_col_count(0)):
                original_values.append(scn.get(indx, row))
            for indx in range(scn.get_col_count(0)):
                scn.set((indx + val) % scn.get_col_count(0), row, original_values[indx])
cnt = 0
for y in range(scn.get_row_count()):
    for x in range(scn.get_col_count(y)):
        cnt += 1 if scn.get(x, y) == '#' else 0
print(cnt)
scn.draw()
