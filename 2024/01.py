from file_helpers import get_all_lines

inputs = get_all_lines("01.txt")
left = []
right = []
for i in inputs:
    parts = i.split(' ')
    left.append(int(parts[0]))
    right.append(int(parts[3]))

left = sorted(left)
right = sorted(right)

total = 0
for indx, i in enumerate(left):
    total += abs(right[indx] - left[indx])
print(total)

total = 0
for l in left:
    occurrences = len([r for r in right if r == l])
    total += l * occurrences
print(total)
