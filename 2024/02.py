import file_helpers


def is_valid(report):
    dir = 0
    valid = True
    for idx, n in enumerate(report):
        if idx > 0:
            diff = report[idx] - report[idx - 1]
            if dir == 0:
                dir = 1 if diff > 0 else -1
            if dir == 1 and diff < 0:
                valid = False
            if dir == -1 and diff > 0:
                valid = False
            if abs(diff) < 1 or abs(diff) > 3:
                valid = False
    return valid


lines = file_helpers.get_all_lines("02.txt")
cnt = 0
for l in lines:
    p = [int(char) for char in l.split(' ')]
    if is_valid(p):
        cnt += 1
    else:
        for idx in range(0, len(p)):
            new_p = p.copy()
            del new_p[idx]
            if is_valid(new_p):
                cnt += 1
                break
print(cnt)
