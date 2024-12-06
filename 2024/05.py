from file_helpers import get_all_lines

lines = get_all_lines("05.txt")

pairs = []


def check_pair(left, right):
    for p in pairs:
        if p['left'] == left and p['right'] == right:
            return True
        elif p['left'] == right and p['right'] == left:
            return False
    return True


def is_valid_printout(printout):
    page_is_match = True
    for left_index, left in enumerate(printout):
        for right_index, right in enumerate(printout):
            if left_index < right_index:
                if not check_pair(left, right):
                    return False, left_index, right_index
    return page_is_match, 0, 0


idx = 0
for idx, l in enumerate(lines):
    if l == '': break
    parts = l.split('|')
    pairs.append({'left': int(parts[0]), 'right': int(parts[1])})

total = 0

printouts = []

for i in range(idx + 1, len(lines)):
    pages = [int(p) for p in lines[i].split(',')]
    printouts.append(pages)

for pages in printouts:
    if is_valid_printout(pages)[0]:
        total += pages[len(pages) // 2]

print(total)
total = 0
for p in printouts:
    result = is_valid_printout(p)

    if not result[0]:
        while not result[0]:
            p[result[1]], p[result[2]] = p[result[2]], p[result[1]]
            result = is_valid_printout(p)
        total += p[len(p) // 2]

print(total)
