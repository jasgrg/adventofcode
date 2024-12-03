from file_helpers import read_all_text
from utlities import regex_findall


def multiply(m):
    m = m.replace("mul(", "").replace(")", "")
    parts = m.split(',')
    return int(parts[0]) * int(parts[1])


input = read_all_text("03.txt")
muls = regex_findall(input, "mul\(\d+,\d+\)")
total = 0
for m in muls:
    total += multiply(m)
print(total)
total = 0
matches = regex_findall(input, "(do\(\)|don't\(\)|mul\(\d+,\d+\))")
enabled = True
for m in matches:
    if m == "do()":
        enabled = True
    elif m == "don't()":
        enabled = False
    else:
        if enabled:
            total += multiply(m)
print(total)
